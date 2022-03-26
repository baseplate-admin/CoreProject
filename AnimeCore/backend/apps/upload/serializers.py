from rest_framework import serializers

from .models import (
    AnimeInfoModel,
    EpisodeCommentModel,
    EpisodeModel,
    EpisodeTimestampModel,
)


class EpisodeTimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeTimestampModel
        exclude = (
            "id",
            "episode_number",
        )


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeCommentModel
        exclude = ("id",)


class EpisodeSerializer(serializers.ModelSerializer):
    episode_comments = EpisodeCommentSerializer(many=True)
    episode_timestamps = EpisodeTimestampSerializer(many=True)

    class Meta:
        model = EpisodeModel
        exclude = ("id",)
        read_only_fields = (
            "episode_number",
            "episode_name",
            "episode_cover",
            "episode_file",
            "episode_summary",
        )

    def update(self, instance: EpisodeModel, validated_data) -> dict:
        """
        {
            "episode_comments": [],
            "episode_timestamps": [{
                "timestamp": 10800,
                "episode_number": 1,
                "user": 1
            }]
        }
        """
        user = self.context["request"].user

        episode_timestamps = validated_data.get("episode_timestamps", None)
        if episode_timestamps:
            for item in episode_timestamps:
                (
                    timestamp_model,
                    timestamp_model_created,
                ) = EpisodeTimestampModel.objects.update_or_create(
                    user=user,
                    defaults={
                        "episode_number": instance.episode_number,
                        "timestamp": item["timestamp"],
                    },
                )
                timestamp_model.save()

                if timestamp_model_created:
                    instance.episode_timestamps.add(timestamp_model)

        return validated_data

    def to_representation(self, instance):
        serializer = super().to_representation(instance)
        try:
            timestamp_query = instance.episode_timestamps.get(
                user=self.context["request"].user
            )
            serializer["episode_timestamps"] = EpisodeTimestampSerializer(
                timestamp_query,
                many=True,
            ).data

        except instance.episode_timestamps.model.DoesNotExist:
            pass

        finally:
            return serializer


class AnimeInfoSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"

    def create(self, validated_data):
        """
        {
            "episodes": [],
            "mal_id": 91328,
            "anime_name": "Gintama",
            "anime_name_japanese": "dsadas",
            "anime_source": "dsaasd",
            "anime_aired_from": "2022-03-22T18:55:17.825914Z",
            "anime_aired_to": "2022-03-22T18:55:17.843866Z",
            "anime_cover": null,
            "updated": "2022-03-21T20:24:48.661105Z"
        }
        """
        validated_data.pop("episodes", None)  # ignore

        data = AnimeInfoModel(**validated_data)
        data.save()

        return data
