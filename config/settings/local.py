from .base import *

DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', 'd8202ab9.ngrok.io', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'social_website_db',
        'USER': 'postgres',
        'PASSWORD': 'CARLYN2128',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

INSTALLED_APPS += [
    'sslserver',  # this will turn http to https, by providing ssl certificate
    'django_extensions',
]

SECURE_SSL_REDIRECT = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST: 'localhost'
EMAIL_PORT: 1025
EMAIL_HOST_USER: ''
EMAIL_HOST_PASSWORD: ''
EMAIL_USE_TLS: ''
EMAIL_USE_SSL: ''

SOCIAL_AUTH_FACEBOOK_KEY = '266394497724340'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'bbae85c4e998bbb502dfa6aca5264d5a'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '428595856531-9i59c7ls6a0t2od9h109d65mdrjdkv8v.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'w0JHrgGcveZYiPeVS2uJ5KdH'  # Google Consumer Secret

"""
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
"""

"""
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}
"""
