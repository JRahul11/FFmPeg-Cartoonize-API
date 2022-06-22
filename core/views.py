from rest_framework.views import APIView
from rest_framework.response import Response

from tigbar.settings import BASE_DIR
from core.models import VideoModel
from core.tasks import processVideo


class CartoonizeVideo(APIView):
        
    def post(self, request):
        user_id = int(request.data['user_id'])
        video = request.FILES['video']

        # Save Original Video to DB and get relative path for input and output
        videoObject = VideoModel.objects.create(user_id=user_id, original_video=video)
        fileName = videoObject.original_video.name.split('/')[1]
        inputPath = str(BASE_DIR) + videoObject.original_video.url
        outputPath = str(BASE_DIR) + '\\media\\tempFiles\\' + fileName

        # Call FFmPeg
        processVideo.delay(inputPath, outputPath, user_id)

        return Response("Processing Video...", status=200)
