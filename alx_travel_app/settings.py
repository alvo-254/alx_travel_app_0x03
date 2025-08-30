# Celery + RabbitMQ configuration
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = "rpc://"

INSTALLED_APPS += [
    "django_celery_beat",
]

# Django email backend (using console for dev, SMTP for prod)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"   # or your provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_password"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
