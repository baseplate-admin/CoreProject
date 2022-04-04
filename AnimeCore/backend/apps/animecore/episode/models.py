from pathlib import Path

from django.db import models
from ..episode_comment.models import EpisodeCommentModel

# Create your models here.


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime

    @staticmethod
    def episode_cover(instance, filename) -> str:
        return Path("episode_cover", filename)

    @staticmethod
    def episode_upload(instance, filename) -> str:
        return Path("episode", filename)


class EpisodeModel(models.Model):
    episode_number = models.BigIntegerField(default=0)
    episode_name = models.CharField(max_length=1024, db_index=True)
    episode_cover = models.ImageField(
        upload_to=FileField.episode_cover, default=None, blank=True, null=True
    )
    episode_file = models.FileField(
        upload_to=FileField.episode_upload, default=None, blank=True, null=True
    )
    episode_summary = models.TextField(default="", blank=True, null=True)
    episode_comments = models.ManyToManyField(EpisodeCommentModel, blank=True)

    def __str__(self) -> str:
        return f"{self.episode_number}. {self.episode_name}"

    class Meta:
        verbose_name = "Episode"
