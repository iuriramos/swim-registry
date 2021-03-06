from .base import *
import dj_database_url

# Database settings
DATABASES = {
    'default': dj_database_url.config()
}

STATICFILES_STORAGE ='whitenoise.django.GzipManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATICFILES_DIRS = (
    BASE_DIR.child('website').child('static'),
    BASE_DIR.child('registry').child('static'),
)

ALLOWED_HOSTS = ['.herokuapp.com', ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

# CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'

DEBUG = False

