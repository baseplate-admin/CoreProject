# Generated by Django 4.0.3 on 2022-03-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0037_animeinfomodel_anime_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animeinfomodel",
            name="anime_rating",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]