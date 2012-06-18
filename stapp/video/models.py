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

class Profile(models.Model):
    """User Profile describes data/information about regirstered user."""
    user = models.OneToOneField(User)
    roll_number = models.CharField(max_length=20)
    institute = models.CharField(max_length=128)
    department = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
