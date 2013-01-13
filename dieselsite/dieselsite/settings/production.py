import os

from common import *

DEBUG = TEMPLATE_DEBUG = False

SECRET_KEY = os.environ.get('DIESELROBIN_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath(os.path.join('tmp', 'dieselrobin.db')),
    }
}
