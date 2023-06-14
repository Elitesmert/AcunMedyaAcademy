# Generated by Django 4.2.2 on 2023-06-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_videocommentmodel_parent'),
        ('account', '0003_rename_department_customusermodel_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Dönem',
                'verbose_name_plural': 'Dönemler',
                'db_table': 'periods',
            },
        ),
        migrations.RenameModel(
            old_name='DepartmentModel',
            new_name='CoursesModel',
        ),
        migrations.AlterModelTable(
            name='coursesmodel',
            table='courses',
        ),
    ]
