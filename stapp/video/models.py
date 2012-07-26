from django.db import models
from django.db.models.signals import post_delete
from signals import delete_files
from taggit.managers import TaggableManager

from base64 import b32encode
from hashlib import sha1
from random import random
import settings

import uuid
import datetime
import Image, os

def pkgen():
    rude = ('lol',)
    bad_pk = True
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:6]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/videos', filename)

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("uploads/screenshots", filename)

class Video(models.Model):
    """Videos to be uploaded.."""
    name = models.CharField(max_length=128)
    filename = models.FileField(upload_to=get_file_path)
    image = models.ImageField(upload_to=get_image_path)
    description = models.TextField()
    mykey = models.CharField(max_length=6, default=pkgen)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name

    

#Call the delete_files signal to delete physical files on delete of record
post_delete.connect(delete_files, Video)

    

class Module(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    video_list = models.ManyToManyField(Video)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.modified = datetime.datetime.today()
        super(Module, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

