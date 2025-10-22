from django.apps import AppConfig


class AnaliticalServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analitical_service'
    def ready(self):
        import analitical_service.signals