from pathlib import Path


from django.db import models
from apps.animecore.anime_characters.models import AnimeCharacterModel
from apps.animecore.anime_genres.models import AnimeGenreModel
from apps.animecore.anime_producers.models import AnimeProducerModel
from apps.animecore.anime_studios.models import AnimeStudioModel
from apps.animecore.anime_synonyms.models import AnimeSynonymModel
from apps.animecore.anime_themes.models import AnimeThemeModel

from apps.animecore.episode.models import EpisodeModel


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def anime_cover(instance, filename) -> str:
        return Path("anime_cover", filename)


# Create your models here.


class AnimeInfoModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=False)
    # anilist_id = models.IntegerField(unique=True, blank=False, null=False)
    anime_name = models.CharField(max_length=1024, db_index=True)
    anime_name_japanese = models.CharField(max_length=1024, null=True, db_index=True)
    anime_source = models.CharField(max_length=128, blank=True, null=True)
    anime_aired_from = models.DateTimeField(blank=True, null=True)
    anime_aired_to = models.DateTimeField(blank=True, null=True)
    anime_cover = models.ImageField(
        upload_to=FileField.anime_cover, default=None, blank=True, null=True
    )
    anime_synopsis = models.TextField(blank=True, null=True)
    anime_background = models.TextField(blank=True, null=True)
    anime_rating = models.CharField(max_length=50, blank=True, null=True)

    anime_episodes = models.ManyToManyField(EpisodeModel, blank=True)
    anime_genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    anime_themes = models.ManyToManyField(AnimeThemeModel, blank=True)
    anime_studios = models.ManyToManyField(AnimeStudioModel, blank=True)
    anime_producers = models.ManyToManyField(AnimeProducerModel, blank=True)
    anime_name_synonyms = models.ManyToManyField(AnimeSynonymModel, blank=True)
    anime_characters = models.ManyToManyField(AnimeCharacterModel, blank=True)

    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"
