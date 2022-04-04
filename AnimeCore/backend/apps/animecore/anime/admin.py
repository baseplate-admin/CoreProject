from django.contrib import admin

from .models import (
    AnimeInfoModel,
)

# Register your models here.


admin.site.register(
    [
        AnimeInfoModel,
    ]
)
