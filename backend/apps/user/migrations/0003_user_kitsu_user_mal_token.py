# Generated by Django 4.0.4 on 2022-05-25 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_video_volume"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="kitsu",
            field=models.JSONField(
                default={
                    "access_token": "",
                    "created_at": 0,
                    "expires_in": 0,
                    "refresh_token": "",
                },
                verbose_name="kitsu",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="mal_token",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]