"""
Django settings for budget_project project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.0', '0.0.0.0']


# Application definition
def build_apps():
    INSTALLED_APPS = []

    PROJECT_APPS = [
        'budget_app', # Original App which creates project entities. Should rename.
        'events', # App which holds event types
        'activities', # App which holds activity types
        'msGraph', # App which holds MS Graph/Azure Types
    ]

    BASE_APPS = [
        # Base applications
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

    ]

    THIRD_PARTY_APPS = [
        # Third Party Apps
        'polymorphic',
    ]

    THEME_APPS = [
        # Apps related to GUI
        'app_theme'
    ]

    FUTURE_APPS = [
        # Apps to be developed in the future and acting as place holders.
        'future',
        #'erp_program.future.approvals',
        #'erp_program.future.reports',
        #'erp_program.future.data_explorer',
    ]

    PRIVILEGED = []
    # Decide if privileged apps will run:
    # access = (env('a2dam')) #Debugging. TODO Remove
    if env('a2dam'): PRIVILEGED.append('a2dam') # TODO Automate this in the future

    CONTAINER = [BASE_APPS, PROJECT_APPS, THIRD_PARTY_APPS, THEME_APPS, FUTURE_APPS, PRIVILEGED]


    for Set in CONTAINER:
        for item in Set:
            INSTALLED_APPS.append(item)
    return INSTALLED_APPS

INSTALLED_APPS = build_apps()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'budget_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'budget_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('erp_NAME'),
        'USER': env('erp_USER'),
        'PASSWORD': env('erp_PASSWORD'),
        'HOST': env('erp_HOST'),
        'PORT': env('erp_PORT'),
    },
    'a2dam': {
        'ENGINE': env('a2dam_ENGINE'),
        'NAME': env('a2dam_NAME'),
        'USER': env('a2dam_USER'),
        'PASSWORD': env('a2dam_PASSWORD'),
        'HOST': env('a2dam_HOST'),
        'PORT': env('a2dam_PORT'),
    },
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

#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = "d/m/Y H:s"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'bootstrap'),
    ]
LOGIN_REDIRECT_URL = 'index'
