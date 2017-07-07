from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+hj7jzxol9(_s+%jh_j%1v__q=gz1!%2a(0e9uzp3ki4j)*816'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Django Debug Toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}
DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    'cachalot.panels.CachalotPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
]

try:
    from .local import *
except ImportError:
    pass
