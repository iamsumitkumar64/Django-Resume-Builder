# Generated by Django 5.1.2 on 2025-01-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='password',
        ),
        migrations.AlterField(
            model_name='user_data',
            name='intro_image',
            field=models.FileField(default=None, null=True, upload_to='user_images/', verbose_name='Enter User Image'),
        ),
    ]
