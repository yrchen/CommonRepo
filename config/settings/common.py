# -*- coding: utf-8 -*-
"""
Django settings for Common Repository project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ

from urlparse import urlparse

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('commonrepo')

env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'grappelli',  # django-grappelli
    'filebrowser',  # django-filebrowser
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts

    # Authentication
    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Google
    # OAuth
    'oauth2_provider',  # Django OAuth Toolkit

    # Django REST Framework
    'rest_framework',  # REST framework
    'rest_framework.authtoken',  # REST framework Token-based authentication
    'rest_framework_tracking',  # DRF tracking
    'rest_framework_swagger',  # Django REST Swagger
    'djoser',  # authentication

    # Comments
    'fluent_comments',  # django-fluent-comments
    'threadedcomments',  # django-threadedcomments
    'django_comments',  # django-contrib-comments

    # Search
    'haystack',  # django-haystack

    # Other tools
    'easy_thumbnails',  # easy-thumbnails (required by django-filer)
    'filer',  # django-filer
    'mptt',  # django-mptt
    'avatar',  # django-avatar
    'annoying',  # django-annoying
    'messages_extends',  # django-messages-extends
    'notifications',  # django-notifications-hq
    'bootstrap_pagination',  # django-bootstrap-pagination
    'reversion',  # django-reversion
    'reversion_compare',  # django-reversion-compare
    'licenses',  # django-licenses
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'commonrepo.users',  # CommonRepo custom users app

    # CommonRepo common apps
    'commonrepo.main',

    # CommonRepo custom apps
    'commonrepo.elos',
    'commonrepo.groups',

    # CommonRepo API endpoints
    'commonrepo.snippets_api',
    'commonrepo.users_api',
    'commonrepo.elos_api',
    'commonrepo.groups_api',

)

THIRD_PARTY_APPS2 = (
    # django-activity-stream
    'actstream',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + THIRD_PARTY_APPS2

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'commonrepo.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Xaver Y.R. Chen""", 'yrchen@ATCity.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    # 'default': env.db("DATABASE_URL", default="postgres:///commonrepo")
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db/development.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        # 'OPTIONS': {
        #     'init_command': 'SET storage_engine=InnoDB',
        #     'charset' : 'utf8',
        #     'use_unicode' : True,
        # },
        # 'TEST_CHARSET': 'utf8',
        # 'TEST_COLLATION': 'utf8_general_ci',
    },
    'mongodb': {
        'ENGINE': '',
    },
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

MONGODB_DATABASES = {
    'default': {
        'ENGINE': '',
    },
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Taipei'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
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

# CELERY
INSTALLED_APPS += ('commonrepo.taskapp.celery.CeleryConfig',)
# if you are not using the django database broker (e.g. rabbitmq, redis, memcached), you can remove the next line.
INSTALLED_APPS += ('kombu.transport.django',)
BROKER_URL = env("CELERY_BROKER_URL", default='django://')
# END CELERY

# Your common stuff: Below this line define 3rd party library settings

# Allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            # https://developers.google.com/+/web/api/rest/oauth
            'profile', 'email',
            # https://www.googleapis.com/discovery/v1/apis/oauth2/v2/rest?fields=auth(oauth2(scopes))
            'https://www.googleapis.com/auth/plus.login',  # Know your basic profile info and list of people in your circles.
            'https://www.googleapis.com/auth/plus.me',  # Know who you are on Google
            ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        }
    }
}

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# Django Activity Stream
ACTSTREAM_SETTINGS = {
    'MANAGER': 'actstream.managers.ActionManager',
    'FETCH_RELATIONS': False,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

# Avatar
AVATAR_STORAGE_DIR = 'avatar'

# Comments
COMMENTS_APP = 'fluent_comments'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url', 'title')
AKISMET_API_KEY = "your-api-key"
# AKISMET_BLOG_URL = "http://example.com"         # Optional, to override auto detection
AKISMET_IS_TEST = False                         # Enable to make test runs

FLUENT_CONTENTS_USE_AKISMET = True              # Enabled by default when AKISMET_API_KEY is set.
FLUENT_COMMENTS_CLOSE_AFTER_DAYS = None         # Auto-close comments after N days
FLUENT_COMMENTS_MODERATE_AFTER_DAYS = None      # Auto-moderate comments after N days.
FLUENT_COMMENTS_AKISMET_ACTION = 'moderate'     # Set to 'moderate' or 'delete'
FLUENT_COMMENTS_USE_EMAIL_NOTIFICATION = False

# Message
MESSAGE_STORAGE = 'messages_extends.storages.FallbackStorage'

# Django Grappelli
GRAPPELLI_ADMIN_TITLE = "Common Repository | Administration"
GRAPPELLI_SWITCH_USER = True

# easy_thumbnails
THUMBNAIL_HIGH_RESOLUTION = True

# Files (django-filer)
FILER_CANONICAL_URL = 'sharing/'

# Documents (django-rest-swagger)
SWAGGER_SETTINGS = {
    """
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': True,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'base_path':'www.commonrepo.com/api/docs/',
    'info': {
        'contact': 'apiteam@wordnik.com',
        'description': 'This is a sample server Petstore server. '
            'You can find out more about Swagger at '
            '<a href="http://swagger.wordnik.com">'
            'http://swagger.wordnik.com</a> '
            'or on irc.freenode.net, #swagger. '
            'For this sample, you can use the api key '
            '"special-key" to test '
            'the authorization filters',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': 'http://helloreverb.com/terms/',
        'title': 'Swagger Sample App',
    },
    'doc_expansion': 'none',
    """
}

# Search (django-haystack)
es = urlparse(env('SEARCHBOX_URL', default="http://127.0.0.1:9200/"))
port = es.port or 80

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': es.scheme + '://' + es.hostname + ':' + str(port),
        'INDEX_NAME': 'documents',
    },
}

if es.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

#
# System config variables
GOOGLE_ANALYTICS_CODE = "UA-71965843-1"
GOOGLE_SITE_VERIFICATION = "cPWx6iSeojj6XLRGYhqDk8DCIFXCwlR7qPn-gIGBHLA"

VERSION = "v0.2.2"

DASHBOARD_MAX_ELOS_MY_PER_PAGE = 8
DASHBOARD_MAX_ELOS_ALL_PER_PAGE = 8
ELOS_MAX_ITEMS_PER_PAGE = 20
GROUPS_MAX_ITEMS_PER_PAGE = 20
USERS_MAX_ELOS_PER_PAGE = 20
USERS_MAX_USERS_PER_PAGE = 20

# ELO
ELO_ROOT_ID = 1
ELO_SIMILARITY_THRESHOLD = 0.5
