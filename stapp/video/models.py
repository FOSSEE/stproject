from django.db import models
from django.contrib.auth.models import User
class Video(models.Model):
    """Videos to be uploaded.."""
    name = models.CharField(max_length=128)
    filename = models.FileField(upload_to="videos")
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    vidio_list = models.ManyToManyField(Video)

    def __unicode__(self):
        return self.name

