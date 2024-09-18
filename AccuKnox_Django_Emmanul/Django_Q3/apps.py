from django.apps import AppConfig


class DjangoQ3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Django_Q3'

def ready(self):
        import Django_Q3.models  # Ensure that signals are registered