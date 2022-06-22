import os
from django.core.files import File
from core.models import VideoModel
from ffmpy import FFmpeg
from celery import shared_task


@shared_task
def processVideo(inputPath, outputPath, user_id):
    ff = FFmpeg(
        inputs={inputPath: None},
        outputs={outputPath: "-vf edgedetect=mode=colormix:low=0.5:high=0.7,eq=brightness=0.20,eq=contrast=2:saturation=3 -pix_fmt yuv420p" }
    )
    ff.run()

    videoObject = VideoModel.objects.get(user_id=user_id, processed_video=None)
    videoObject.processed_video.save(os.path.basename(outputPath), content=File(open(outputPath, 'rb')))
    os.remove(outputPath)