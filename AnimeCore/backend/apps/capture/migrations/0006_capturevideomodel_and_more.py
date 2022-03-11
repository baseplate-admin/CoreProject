# Generated by Django 4.0.3 on 2022-03-11 12:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("capture", "0005_alter_capturevideovolumemodel_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CaptureVideoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "video_volume",
                    models.IntegerField(
                        default=50,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "video_timestamp",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Video Capture Model",
            },
        ),
        migrations.RemoveField(
            model_name="capturevideovolumemodel",
            name="user",
        ),
        migrations.DeleteModel(
            name="CaptureVideoTimeStampModel",
        ),
        migrations.DeleteModel(
            name="CaptureVideoVolumeModel",
        ),
    ]
