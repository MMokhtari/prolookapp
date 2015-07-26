"""
Django settings for prolookapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v(tzqlep9_2t^_p161wyhfe+!0md6pvk6l37_*ow4fhd^swv&q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'corsheaders',
    'rest_framework',
    'AuthAccount',
    'home',
    'workplace',
    'taskmanager',
    'companymanager',
    'employeesmanager',
)
AUTH_USER_MODEL = 'AuthAccount.Account'

AUTHENTICATION_BACKENDS = (
    'AuthAccount.auth_backends.ProlookappBackend',
)
CUSTOM_USER_MODEL = 'AuthAccount.Account'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'prolookapp.urls'

SUBDOMAIN_URLCONFS = {
    None: 'prolookapp.urls.frontend',  # no subdomain, e.g. ``example.com``
    'www': 'prolookapp.urls.frontend',
    'api': 'prolookapp.urls.api',
}

WSGI_APPLICATION = 'prolookapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'prolookapp_db',
        'USER': 'root',
        'PASSWORD': 'prolookapp',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
#rest framework

#'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',), 
# 'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
REST_FRAMEWORK = {    
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENICATION_CLASSES': ('rest_framework.authenication.SessionAuthenication',),
    # 'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',), 
    # 'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'PAGINATE_BY': 10

}
# PASSWORD_HASHERS = (
# 'django.contrib.auth.hashers.MD5PasswordHasher',
# )
# https://ep2014.europython.eu/en/schedule/sessions/81/
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        },
    'loggers': {
        
        'taskmanager': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        }
    }
# if DEBUG:
#     # make all loggers use the console.
#     for logger in LOGGING['loggers']:
#         LOGGING['loggers'][logger]['handlers'] = ['console']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/static/',
)
# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
# MEDIA_URL = "/media/"