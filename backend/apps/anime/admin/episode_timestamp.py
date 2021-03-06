from django.contrib import admin

from ..models import EpisodeTimestampModel

# Register your models here.


@admin.register(EpisodeTimestampModel)
class EpisodeTimestampAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "episode"]
    list_filter = ["user", "episode"]
