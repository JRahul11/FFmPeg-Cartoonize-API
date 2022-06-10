import os
from django.core.files import File
from rest_framework.views import APIView
from rest_framework.response import Response
from ffmpy import FFmpeg
from tigbar.settings import BASE_DIR
from core.models import VideoModel


class CartoonizeVideo(APIView):

    def post(self, request):
        video = request.FILES['video']

        # Save Original Video to DB and get relative path for input and output
        videoObject = VideoModel.objects.create(original_video=video)
        fileName = videoObject.original_video.name.split('/')[1]
        inputPath = str(BASE_DIR) + videoObject.original_video.url
        outputPath = str(BASE_DIR) + '\\media\\tempFiles\\' + fileName

        # Call FFMPEG to process video
        ff = FFmpeg(
            inputs={inputPath: None},
            outputs={outputPath: "-vf edgedetect=mode=colormix:low=0.5:high=0.7,eq=brightness=0.20,eq=contrast=2:saturation=3 -pix_fmt yuv420p" }
        )
        ff.run()

        # Save Processed Video to DB and delete the temp files
        videoObject.processed_video.save(os.path.basename(outputPath), content=File(open(outputPath, 'rb')))
        os.remove(outputPath)

        # Return URL for the processed video
        return Response(
            {
                'original_video': videoObject.original_video.url,
                'processed_video': videoObject.processed_video.url
            }, 
            status=200
        )
