"""
Django settings for allifmain project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u2$rwitrp-bvgkqy=ev*3wji1pxu&%t8@v)e*=503ab*_$!b=l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'jazzmin',
    'django.contrib.admin',# uncomment after migrations
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'crispy_forms',
    
    
    "django.contrib.humanize",
    
   
    "allifapp",
    #'django_select2',
    "allifmaalusersapp",
    "allifmaalloginapp",
    "allifmaaluiapp",
    
   
    
    

    

]
#CRISPY_TEMPLATE_PACK = 'uni_form'
#CRISPY_TEMPLATE_PACK = 'bootstrap4'

# below is for select 2
#CACHES = {
    # … default cache config and others
    #"select2": {
      #  "BACKEND": "django_redis.cache.RedisCache",
       # "LOCATION": "redis://127.0.0.1:6379/2",
       # "OPTIONS": {
         #   "CLIENT_CLASS": "django_redis.client.DefaultClient",
       # }
   # }
#}

# Tell select2 which cache configuration to use:
#SELECT2_CACHE_BACKEND = "select2"

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Alwen Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Alwen",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Alwen Transport",

    # Logo to use for your site, must be present in static files, used for brand on top left
    #"site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Allifmaal Applications",

    # Copyright on the footer
    "copyright": "Allifmaal",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'allifmain.urls'


# below is for auto logout when there is inactivity... there is two ways to do it as below.
#AUTO_LOGOUT = {'IDLE_TIME': 60}  # logout after 10 minutes of downtime
from datetime import timedelta
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=10),
    'login:userLoginPage': True,
}

# django_project/settings.py
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'allifapp.preprocessor.globalVariables',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'allifmain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'allifmaal_db',
        'USER': 'root',
        'PASSWORD': 'amd30974153',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}  
"""

"""... below worked for me as of 22nd feb 2024
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MYSQL',
        'USER': 'root',
        'PASSWORD': 'hidden',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}  

"""


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Mogadishu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_LOCATION='static'

#STATIC_URL = '/static/'
#STATIC_ROOT='static'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]


#PATH WHERE UPLOADED FILES WILL BE STORED...in the media folder
MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')
MEDIA_URL='/media/'#fetch images/media using this path when viewing through the browser...this folder will be created automatically when we upload the first image
AUTH_USER_MODEL = 'allifmaalusersapp.User'
#SENDSMS_BACKEND = 'allifmaalusersapp.mysmsbackend.SmsBackend'