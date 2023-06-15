from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUserModel, StudentModel

@receiver(post_save, sender=CustomUserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.groups == 1:
            StudentModel.objects.create(user=instance)