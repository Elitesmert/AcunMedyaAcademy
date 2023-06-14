from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.videos'
    verbose_name = 'Video Yönetimi'

    def ready(self):
        from .signals import send_discord_message