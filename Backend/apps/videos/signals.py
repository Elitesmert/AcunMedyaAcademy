from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VideoModel
from discord_webhook import DiscordWebhook
from django.conf import settings


@receiver(post_save, sender=VideoModel)  # VideoModel, video modelinizi temsil eden model adı ile değiştirin
def send_discord_message(sender, instance, created, **kwargs):
    webhook_url = "https://discord.com/api/webhooks/1117070557117165578" \
                  "/Js0tR8skdwMxJi6_3Po_GVV0kg9ykySqWdlpqkJ7O2uioLjCStJXZ6jbQlxin1G1Gpnf"
    user_name = instance.instructor.username
    video_title = instance.title
    video = instance.video_file
    SITE_URL = 'https://furkanozay.tech/'
    if created:
        message = f"{user_name}, {video_title} isminde yeni bir video paylaştı\nizlemek için: {SITE_URL}{settings.MEDIA_URL}{video}"
        webhook = DiscordWebhook(url=webhook_url, content=message)
        webhook.execute()
    else:
        message = f"**{video_title}**, isimli video **{user_name}** {SITE_URL}media/{video} tarafından düzenlendi"
        webhook = DiscordWebhook(url=webhook_url, content=message)
        webhook.execute()
