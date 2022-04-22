# Generated by Django 4.0.4 on 2022-04-22 12:08

import apps.anime.models.anime_info
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0003_alter_animerecommendationmodel_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animeinfomodel",
            name="anime_banner",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to=apps.anime.models.anime_info.FileField.anime_banner,
            ),
        ),
    ]