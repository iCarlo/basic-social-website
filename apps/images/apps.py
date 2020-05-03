from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'apps.images'

    def ready(self):
        # import signal handlers
        import apps.images.signals
