# Generated by Django 4.2.2 on 2023-06-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customusermodel_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customusermodel',
            old_name='department',
            new_name='courses',
        ),
    ]
