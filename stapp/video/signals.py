from django.core.files.storage import default_storage

def delete_files(sender, **kwargs):
    """Automatically deleted files when records removed.
    """
    video = kwargs.get('instance')
    #default_storage.delete(school.pdf.path)
    default_storage.delete(video.filename.path)
    default_storage.delete(video.image.path)
    try:
        default_storage.delete(video.thumbnail.path)
    except:
        pass
