from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'https://localhost:9200',
        'http_auth': ('elastic', '123456'),
        'verify_certs': False,
        # 'scheme': 'http'
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}