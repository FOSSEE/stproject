from django.db import models
from django.contrib.auth.models import User
class Video(models.Model):
    """Videos to be uploaded.."""
    video_name = models.CharField(max_length=128)
    video_file = models.FileField(upload_to="videos")
    video_descriotion = models.TextField()

class Module(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    vidio_list = models.ManyToManyField(Video)

class Profile(models.Model):
    """User Profile describes data/information about regirstered user."""
    user = models.OneToOneField(User)
    roll_number = models.CharField(max_length=20)
    institute = models.CharField(max_length=128)
    department = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
