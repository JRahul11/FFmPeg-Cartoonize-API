from django.db import models

class VideoModel(models.Model):
    original_video = models.FileField(upload_to='originalVideos', default=None, blank=True)
    processed_video = models.FileField(upload_to='processedVideos', default=None, blank=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'Videos'