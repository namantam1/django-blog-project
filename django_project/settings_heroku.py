from .settings import *
import django_heroku

INSTALLED_APPS += [
    'cloudinary_storage',
    'cloudinary'
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

django_heroku.settings(locals())
