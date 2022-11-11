from django.apps import AppConfig


class DonationsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "donations"
    verbose_name = "Донаты"

    def ready(self):
        from . import signals
