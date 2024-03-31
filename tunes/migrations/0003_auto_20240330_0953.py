# Generated by Django 3.2.23 on 2024-03-30 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tunes', '0002_watchlater'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlater',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1234, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlater',
            name='song',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='tunes.song'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='watchlater',
            unique_together={('user', 'song')},
        ),
        migrations.RemoveField(
            model_name='watchlater',
            name='video_id',
        ),
        migrations.RemoveField(
            model_name='watchlater',
            name='watch_id',
        ),
    ]
