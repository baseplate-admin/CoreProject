# Generated by Django 4.0.3 on 2022-04-04 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_animecharactermodel_animeproducermodel_and_more'),
        ('anime_characters', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnimeCharacterModel',
        ),
    ]
