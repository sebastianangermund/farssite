"""
Django settings for farssite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v+$z435_(2$uwn%*w3i#rf=^k*5y!yaurll(uy=_%ska)yu1_5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'farssite',
    'rest_framework',
    'farssite.furniture.apps.FurnitureConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'farssite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['farssite/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'farssite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'farssite',
        'USER': 'sebang',
        'PASSWORD': '123Hejsan',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "node_modules"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
    
COMPRESS_OFFLINE = False

COMPRESS_OUTPUT_DIR = ''

try:
    from local_settings import *
except ImportError:
    pass

NODE_ENV = 'development' if DEBUG else 'production'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'node_modules/.bin/node-sass {infile} {outfile}'),
    ('text/jsx', 'NODE_ENV={} node_modules/.bin/browserifyinc '
                 '--debug '
                 '-t babelify {{infile}} -o {{outfile}}'.format(NODE_ENV)),
)

if not DEBUG:
    COMPRESS_OFFLINE = True
    COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'node_modules/.bin/node-sass {infile} {outfile}'),
    ('text/jsx', 'NODE_ENV=production node_modules/.bin/browserify '
                 '-t babelify {infile} -o {outfile}'),
)

ADMINS = (
    ('Sebastian', 'sebastianangermund@gmail.com'),
)

SERVER_EMAIL = 'mail@mail.se'