# Generated by Django 4.2.2 on 2023-06-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customusermodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='username',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
