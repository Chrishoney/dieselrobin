import os

from common import *

SECRET_KEY = os.environ.get('DIESELROBIN_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'dieselrobin',
        'PASSWORD': 'dieselrobin',
        'HOST': '',
        'PORT': '',
    }
}
