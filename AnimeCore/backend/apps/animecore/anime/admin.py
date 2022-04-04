from django.contrib import admin

from .models import (
    AnimeInfoModel,
)

# Register your models here.
class AnimeInfoAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "anime_genres",
        "anime_themes",
        "anime_studios",
        "anime_producers",
        "anime_name_synonyms",
        "anime_characters",
    )


admin.site.register(AnimeInfoModel, AnimeInfoAdmin)
