# Generated by Django 5.1.2 on 2025-04-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_App', '0004_alter_user_data_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='intro_image',
            field=models.TextField(default=''),
        ),
    ]
