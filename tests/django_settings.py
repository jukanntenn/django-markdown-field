# supress RemovedInDjango50Warning
USE_TZ = True

SECRET_KEY = "test-secret-key"

INSTALLED_APPS = ["tests"]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
