from .base import *


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

CELERY_BEAT_SCHEDULE = {
    "scrape": {
        "task": "scraper.tasks.scrape",
        "schedule": crontab(minute="*/20"),
    },
    "loadproducts": {
        "task": "products.tasks.loadproducts",
        "schedule": crontab(minute="*/2"),
    },

    "deleteproducts": {
        "task": "products.tasks.remover_no_stock_products",
        "schedule": crontab(minute="*/25"),
    },
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

