
from stapp.settings import *
DEBUG=True
TEMPLATE_DEBUG=DEBUG

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (

    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)
