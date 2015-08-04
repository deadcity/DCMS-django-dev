"""
Django settings for DCMS project.

Based on generation by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(PROJECT_PATH, ...)
import os
import sys

try:
    from DCMS import platform_settings
except ImportError:
    sys.stderr.write('''
WARNING: Configuration file missing - 'DCMS/platform_settings.py'
    Could not find file 'DCMS/platform_settings.py'. Using default platform-
    settings file 'DCMS/platform_settings_default.py' instead. These will be
    DEBUG configurations with a SQLite database. If you'd like to customize
    that configuration, or simply suppress this warning, make a copy of
    'DCMS/platform_settings_default.py' and save it as
    'DCMS/platform_settings.py'.

''')
    from DCMS import platform_settings_default as platform_settings


PROJECT_PATH = platform_settings.PROJECT_PATH
URL_PREFIX = platform_settings.URL_PREFIX

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = platform_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = platform_settings.DEBUG

ALLOWED_HOSTS = []


##
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'compressor',
    # 'rest_framework',

    'accounts',
    'characters',
    'chronicles',
    'DCMS',
    'dsqla',
    # 'common',
    'trait_access',
    'traits',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'dsqla.middleware.SQLATransactionMiddleware',
)

ROOT_URLCONF = 'DCMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'DCMS.context_processors.url_prefix',
            ]
        }
    }
]

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'DCMS.wsgi.application'


##
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': platform_settings.DATABASES_default
}


##
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


##
# Staticfiles
# Settings for "django.contrib.staticfiles".
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = platform_settings.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = URL_PREFIX + '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)


##
# Auth
# Settings for "django.contrib.auth".

LOGIN_URL = URL_PREFIX + '/accounts/login/'
LOGIN_REDIRECT_URL = URL_PREFIX + '/character/'


##
# SQLAlchemy
# Settings for "DCMS.dsqla".
from DCMS.model_base import BaseModel
DSQLA_BASE_MODEL = BaseModel


##
# Django-compressor
# http://django-compressor.readthedocs.org/en/latest/settings/

if os.name == 'nt':
    COMPRESS_PRECOMPILERS = (
        ('text/coffeescript', 'coffee.cmd --compile --stdio'),
    )
else:
    COMPRESS_PRECOMPILERS = (
        ('text/coffeescript', 'coffee --compile --stdio'),
    )

COMPRESS_ENABLED = platform_settings.COMPRESS_ENABLED
COMPRESS_OFFLINE = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
