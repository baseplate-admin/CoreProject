# Generated by Django 4.0.3 on 2022-03-16 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0020_alter_episodecommentmodel_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episodemodel",
            name="episode_comments",
        ),
    ]