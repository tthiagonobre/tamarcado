# Generated by Django 5.1.4 on 2025-01-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_agendamento_is_canceled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='is_canceled',
            new_name='is_deleted',
        ),
    ]