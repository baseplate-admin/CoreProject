# Generated by Django 4.0.4 on 2022-04-24 02:53
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimeThemeModel",
            fields=[
                (
                    "mal_id",
                    models.IntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default="", max_length=50, unique=True
                    ),
                ),
                ("type", models.CharField(db_index=True, default="", max_length=50)),
            ],
            options={
                "verbose_name": "Anime Theme",
            },
        ),
    ]
