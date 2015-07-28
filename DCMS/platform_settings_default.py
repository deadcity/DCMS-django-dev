from os import path

PROJECT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k*td47e_xdm1%37x*rijje5!2f=lq)k*2ivf=dazw!^2sk#qs*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES_default = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': path.join(PROJECT_PATH, 'DCMS.db'),
}

URL_PREFIX = ''
STATIC_ROOT = ''

COMPRESS_ENABLED = not DEBUG
