import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG = {}

try:
    with open(f"{BASE_DIR}/app-config/config.json", "r") as f:
        CONFIG = json.load(f)
except Exception as e:
    print(f"Error to load config from {BASE_DIR}/app-config/config.json")

MYSQL_CONFIG = CONFIG.get("mysql_db", {})
POSTGRESQL_CONFIG = CONFIG.get("postgres_db", {})
SERVICE_NAME = CONFIG.get("service_name", {})
REDIS_CONFIG = CONFIG.get("redis", {})
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
if MYSQL_CONFIG:
    for db_name, db_data in MYSQL_CONFIG.items():
        db_data.update({
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
            'TEST': {
                'CHARSET': 'utf8mb4',
                'COLLATION': 'utf8mb4_unicode_ci',
            }
        })
        DATABASES.update({
            db_name: db_data
        })
if POSTGRESQL_CONFIG:
    for db_name, db_data in POSTGRESQL_CONFIG.items():
        db_data.update({
            'ENGINE': 'django.db.backends.postgresql',
        })

        DATABASES.update({
            db_name: db_data
        })

DATABASE_ROUTERS = ['djangoapp.db_routers.DbRouter']

if REDIS_CONFIG:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f'redis://{REDIS_CONFIG["host"]}:{REDIS_CONFIG["port"]}/{REDIS_CONFIG["db"]}',
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }
LOG_PATH = f"{BASE_DIR}/logs"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': 'libs.tracing.formatter.DjangoFormatter',
            'datefmt': "%d/%b/%Y-%H:%M:%S"
        }
    },
    'handlers': {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    'loggers': {
        '': {
            'handlers': ["console"],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        "django": {
            'handlers': ["console"],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'CRITICAL'),
        }
    },

}
# AUTHENTICATION_BACKENDS = ['libs.middlewares.authentication.CustomAuthMiddleware']
import pymysql

pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()
