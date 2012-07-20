from video.models import Video, Module
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

# we define our resources to add to admin pages
class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/admin/js/editor.js',
  )
  css = {
    'all': ('/static/admin/css/editor.css',),
  }

# let's add it to this model
site.register(Video,
  list_display = ('description',),
  search_fields = ['description',],
  Media = CommonMedia,
)

site.register(Module,
  list_display = ('description',),
  search_fields = ['description',],
  Media = CommonMedia,
)
#admin.site.register(Video)
#admin.site.register(Module)
