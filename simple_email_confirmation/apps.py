from django.apps import AppConfig

class Config(AppConfig):
    name = "simple_email_confirmation.apps"
    verbose_name = "Simple Email Confirmation"

    def ready(self):
        super(Config, self).ready()
        import simple_email_confirmation.signals  # Import signals
