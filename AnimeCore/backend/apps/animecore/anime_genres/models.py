from django.db import models

# Create your models here.


class AnimeGenreModel(models.Model):
    mal_id = models.IntegerField(
        unique=True, blank=False, null=False, primary_key=True, db_index=True
    )
    name = models.CharField(
        unique=True, max_length=50, default="", null=False, blank=False, db_index=True
    )

    def __str__(self) -> str:
        return f"{self.mal_id}. {self.name}"

    class Meta:
        verbose_name = "Anime Genre"
