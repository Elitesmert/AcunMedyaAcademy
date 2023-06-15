from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUserModel, StudentModel, InstructorModel


@receiver(post_save, sender=CustomUserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        group_name = 'Öğrenci'  # Öğrenci grubunun adını buraya girin
        if instance.groups.name == group_name:
            StudentModel.objects.create(user=instance)
        elif instance.groups.name == 'Eğitmen':
            InstructorModel.objects.create(user=instance)


@receiver(pre_save, sender=CustomUserModel)
def update_profile(sender, instance, **kwargs):
    try:
        old_user = CustomUserModel.objects.get(pk=instance.pk)
        old_group_name = old_user.groups.name
    except CustomUserModel.DoesNotExist:
        return

    new_group_name = instance.groups.name

    if old_group_name != new_group_name:
        if new_group_name == 'Öğrenci':
            StudentModel.objects.create(user=instance)
            InstructorModel.objects.filter(user=instance).delete()
        elif new_group_name == 'Eğitmen':
            InstructorModel.objects.create(user=instance)
            StudentModel.objects.filter(user=instance).delete()


