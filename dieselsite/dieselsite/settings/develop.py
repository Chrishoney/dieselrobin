from common import *

SECRET_KEY = 'XJ0z6(;!u/)8_+s|(T*(}iKeM)BWaS;]:G):;6!}AI=j}AkEWx^u'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'temp.db'),
    }
}

INSTALLED_APPS += (
    'south',
    'django_extensions',
    'diesel',
)
