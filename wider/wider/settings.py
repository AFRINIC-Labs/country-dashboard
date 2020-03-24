import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import wazimap

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o+!(hkp)rfo9uv0wbmel7zo=@70)(oiuniip$k1!_q7t04!515'

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

ROOT_URLCONF = 'wider.urls'

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

WSGI_APPLICATION = 'wider.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wider',
        'USER': 'wider',
        'PASSWORD': 'wider',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Indian/Mauritius'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# WAZIMAP CONFIGURATION

# pull in the default wazimap settings
from wazimap.settings import *

# install this app before Wazimap
INSTALLED_APPS = ['wider'] + INSTALLED_APPS

# Localise this instance of Wazimap
WAZIMAP['name'] = 'Country Dashboard'
# NB: this must be https if your site supports HTTPS.
WAZIMAP['url'] = ''
WAZIMAP['country_code'] = 'AF'

WAZIMAP['versions'] = ['2018-03', '2019-03']

WAZIMAP['comparative_levels'] = ['country']

WAZIMAP['geometry_data'] = {
    '2018-03': {
        'continent': 'geo/continent.topojson',
        'country': 'geo/country.topojson'
    }
}

WAZIMAP['default_geo_version'] = None
WAZIMAP['profile_builder'] = 'wazimap_ww.profiles.get_profile'
WAZIMAP['geodata']: 'wazimap.geo.GeoData'
WAZIMAP['map_centre']: None
WAZIMAP['map_zoom']: None

STRIP_WWW = True
USE_THOUSAND_SEPARATOR = True

if DEBUG:
    CSRF_COOKIE_SECURE = False

