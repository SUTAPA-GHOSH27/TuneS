# Generated by Django 3.2.23 on 2024-03-30 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0004_alter_watchlater_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlater',
            old_name='id',
            new_name='watch_id',
        ),
        migrations.AlterUniqueTogether(
            name='watchlater',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='watchlater',
            name='song',
        ),
    ]
