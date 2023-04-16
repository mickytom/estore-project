from django.apps import AppConfig


class EstorappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Estorapp'
    def ready(self):

        import Estorapp.signals