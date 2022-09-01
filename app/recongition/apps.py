from django.apps import AppConfig


class RecongitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recongition'

    def ready(self):
        print('hi')
