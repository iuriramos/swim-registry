from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'swim_registry',
        'USER': get_env_variable('POSTGRES_USER'),
        'PASSWORD': get_env_variable('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_STORAGE ='whitenoise.django.GzipManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')

STATICFILES_DIRS = (
    BASE_DIR.child('website').child('static'),
    BASE_DIR.child('registry').child('static'),
)

ALLOWED_HOSTS = ['164.41.76.94', '127.0.0.1', 'localhost', ]

DEBUG = True

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF_COOKIE_SECURE = True

# SESSION_COOKIE_SECURE = True

# SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_BROWSER_XSS_FILTER = True

# SECURE_SSL_REDIRECT = True

# X_FRAME_OPTIONS = 'DENY'

