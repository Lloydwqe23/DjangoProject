# Generated by Django 4.1.1 on 2023-02-24 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0002_usersettings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersettings',
            old_name='send_push',
            new_name='is_send_push',
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]