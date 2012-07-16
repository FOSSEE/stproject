from django.db import models
from django.db.models.signals import post_delete
from signals import delete_files

import settings


import datetime
import Image, os

def handle_thumb(image_obj, thumb_obj, width, height):
    # create thumbnail
    if image_obj and not thumb_obj:
        thumb = image_obj.path + ('-small.jpg')
        #try:
        t = Image.open(image_obj.path)

        w, h = t.size
        if float(w)/h < float(width)/height:
            t = t.resize((width, h*width/w), Image.ANTIALIAS)
        else:
            t = t.resize((w*height/h, height), Image.ANTIALIAS)
        w, h = t.size
        t = t.crop( ((w-width)/2, (h-height)/4, (w-width)/2+width, \
            (h-height)/4+height) )

        t.save(settings.MEDIA_ROOT + thumb, 'JPEG')
        os.chmod(settings.MEDIA_ROOT + thumb, 0666)
        thumb_obj = image_obj.url + ('-small.jpg')
        #except:
        #    pass
    return thumb_obj


class Video(models.Model):
    """Videos to be uploaded.."""
    name = models.CharField(max_length=128)
    filename = models.FileField(upload_to="uploads/videos")
    image = models.ImageField(upload_to="uploads/screenshots")
    thumbnail = models.ImageField(upload_to='uploads/screenshots', \
        blank=True, null=True, editable=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        '''On save, generate thumbnails'''
        super(Video, self).save()
        self.thumbnail = handle_thumb(self.image, self.thumbnail, 100, 100)
        super(Video, self).save(force_update=True)

#Call the delete_files signal to delete physical files on delete of record
post_delete.connect(delete_files, Video)

    

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

