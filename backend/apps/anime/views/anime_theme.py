from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import AnimeInfoModel
from ..permissions import IsSuperUserOrReadOnly
from ..serializers import AnimeThemeSerializer


class AnimeThemeView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    """
    Returns :
        - Themes
    """

    serializer_class = AnimeThemeSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        instance = AnimeInfoModel.objects.all()
        queryset = get_object_or_404(
            instance, pk=self.kwargs["anime_id"]
        ).anime_genres.all()

        return queryset

    def get_serializer_context(self):
        # Thanks StackOverFlow
        # https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
        context = super().get_serializer_context()
        context.update(
            {"anime_id": self.kwargs.get("anime_id")},
        )
        return context
