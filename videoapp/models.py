from django.db import models

# Create your models here.

class VideoModel(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="files")
    postdate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title