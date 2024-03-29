# Django settings for pentathlon project.
from settings_default import *
UNIQUE_PREFIX = 'pentathlon_production'

# ##############################################################################
# remove before flight
# ##############################################################################
raise Exception('Production not yet configured.')

DEPLOYMENT = {
    'git_repository': 'git@github.com:allink/pentathlon.git',
    'git_branch': 'master',
    'git_remote': 'origin',
    'hosts': ['.nine.ch'],
    'user': 'www-data',
    'project': 'pentathlon',
    'root': '/home/www-data/projects',
    'celery_worker': '%s_celery' % UNIQUE_PREFIX,
    'rabbitmq_vhost': UNIQUE_PREFIX,
    'rabbitmq_username': UNIQUE_PREFIX,
    'rabbitmq_password': '52d098vfn13',
    'is_stage': False,
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_%s' % UNIQUE_PREFIX,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES += ('pentathlon.middleware.ValidateHostMiddleware',)

ADMINS = (
    ('itcrowd', 'itcrowd@allink.ch'),
)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': UNIQUE_PREFIX,
        'VERSION': 1,
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# broker and celery
BROKER_URL = 'amqp://%(rabbitmq_username)s:%(rabbitmq_password)s@localhost:5672/%(rabbitmq_vhost)s' % DEPLOYMENT
CELERY_RESULT_BACKEND = "redis://localhost/0"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERYD_CONCURRENCY = 1
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True

# sentry
RAVEN_CONFIG = {
    'dsn': '',
}
