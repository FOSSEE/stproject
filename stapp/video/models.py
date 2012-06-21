from django.db import models
from django.contrib.auth.models import User
import datetime

class Video(models.Model):
    """Videos to be uploaded.."""
    name = models.CharField(max_length=128)
    filename = models.FileField(upload_to="videos")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    video_list = models.ManyToManyField(Video)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.modified = datetime.datetime.today()
        super(Module, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

