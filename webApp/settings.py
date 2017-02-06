"""
Django settings for babyblog project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap3',
    'django_extensions',
    'babyblog',
    'zn_auth',
    'rest_framework',
    'corsheaders',
    'oauth2_provider',
)

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        # 'groups': 'Access to your groups'
    }
}

REST_FRAMEWORK = {
    # django-oauth-toolkit permissions
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.authentication.BasicAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        # 'rest_framework.parsers.MultiPartParser',
        # 'rest_framework.parsers.FileUploadParser',
        # 'rest_framework.parsers.FormParser',
    ),
    # 'PAGE_SIZE': 10,
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    # END CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # To get informed of generated 404 pages
    'django.middleware.common.BrokenLinkEmailsMiddleware'
)

ROOT_URLCONF = 'webApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
        ],
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

WSGI_APPLICATION = 'webApp.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/s/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
LOGIN_URL = reverse_lazy('zn_auth:login')
LOGIN_REDIRECT_URL = reverse_lazy('babyblog:home')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/m/'


# Define settings configuration (dev or prod)
HOST = socket.gethostname()
if HOST != 'vps121400.ovh.net':
    # Dev settings
    SITE_ID = 1
    DEBUG = True
    TEMPLATES[0]['OPTIONS']['debug'] = True,
    SECRET_KEY = 'development_settings_secret_key'
    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    CORS_ORIGIN_ALLOW_ALL = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Prod settings
    TEMPLATES[0]['OPTIONS']['debug'] = False
    from .production import *
