from __future__ import absolute_import, unicode_literals

from .base import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{ cookiecutter.domain_name }}'])
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = False

# Template caching
TEMPLATES[0]['APP_DIRS'] = False
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# Static/media files settings
STORAGE_DIR = ROOT_DIR.path('storage')
STATIC_ROOT = str(STORAGE_DIR.path('static'))
MEDIA_ROOT = str(STORAGE_DIR.path('media'))

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        }
    }
}

# Mail
INSTALLED_APPS += [
    'anymail'
]
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', '{{ cookiecutter.email }}')
ANYMAIL = {
    'MAILGUN_API_KEY': os.getenv('MAILGUN_API_KEY'),
    'MAILGUN_SEND_DEFAULTS': {
        'esp_extra': {'sender_domain': 'mg.{{ cookiecutter.domain_name }}'}
    }
}

try:
    from .local import *
except ImportError:
    pass
