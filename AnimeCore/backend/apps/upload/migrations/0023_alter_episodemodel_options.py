# Generated by Django 4.0.3 on 2022-03-17 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0022_episodemodel_episode_comments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="episodemodel",
            options={"ordering": ("-episode_number",), "verbose_name": "Episode info"},
        ),
    ]