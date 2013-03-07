from time import time
from django.utils.http import http_date

__author__ = 'arnaud'



# Django settings for next_pope project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
 ('Arnaud BRETON', 'arnaud@unishared.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/next_pope', )
}
DATABASES['default'].update({
    'OPTIONS': {'autocommit': True,}
})

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['next-pope.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'media'



# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static'



# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

if not DEBUG:
    # Django pipeline settings
    PIPELINE = True
    STATICFILES_STORAGE = 'quizz.amazons3.CloudfrontCachedPipelineStaticStorage'
    DEFAULT_FILE_STORAGE = 'quizz.amazons3.CloudfrontMediaStorage'

    DEFAULT_S3_PATH = "media"
    STATIC_S3_PATH = "static"
    AWS_STORAGE_BUCKET_NAME = 'next-pope'
    AWS_BUCKET_URL = '//{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

    STATIC_URL = AWS_BUCKET_URL + '/%s/' % STATIC_S3_PATH
    MEDIA_URL = AWS_BUCKET_URL + '/%s/' % DEFAULT_S3_PATH
else:
    # URL prefix for static files.
    STATIC_URL = '/static/'
    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    MEDIA_URL = '/media/'

# Amazon Web Services configuration
AWS_ACCESS_KEY_ID = 'AKIAIRC6TOAJKJJPCVJA'
AWS_SECRET_ACCESS_KEY = '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'
max_age = 315360000
AWS_HEADERS = {
    'x-amz-acl': 'public-read',
    'Expires': http_date(time() + max_age),
    'Cache-Control': 'public, max-age=' + str(max_age)
}

AWS_S3_SECURE_URLS = False
AWS_IS_GZIPPED = True
AWS_QUERYSTRING_AUTH = False

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'quizz.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'quizz.wsgi.application'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

SECRET_KEY = "next=y^4y6n*kn#e@on2e(^-u9%)n9lbb58r7mg26)tu_xm)j=)#lipope"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
            },
        'console': {
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
            'stream'  : 'ext://sys.stdout',
            'formatter': 'verbose'
        },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
            },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        },
    }
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quizz',
    'south',
    'boto',
    'storages',
    'gunicorn'
    )

"""
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quizz',
    'social_auth',
    'sorl.thumbnail',
    'south',
    'pipeline',
    'require',
    'herokuapp',
    )
"""