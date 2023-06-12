from django.db import models
from django.utils import timezone

from ..account.models import CustomUserModel


class UsefulLinksModel(models.Model):
    LANGUAGE_CHOICES = [
        ("tr", "Türkçe"),
        ("en", "İngilizce"),
    ]
    name = models.CharField(max_length=150)
    link = models.URLField(max_length=180)
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='links',
                               limit_choices_to={"groups": 2})
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=4)
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)

    class Meta:
        db_table = 'useful_links'
        verbose_name = 'Faydalı Link'
        verbose_name_plural = 'Faydalı Linkler'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        return super(UsefulLinksModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
