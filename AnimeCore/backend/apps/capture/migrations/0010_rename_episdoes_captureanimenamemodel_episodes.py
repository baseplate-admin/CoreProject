# Generated by Django 4.0.3 on 2022-03-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("capture", "0009_rename_timestamp_capturevideomodel_timestamps"),
    ]

    operations = [
        migrations.RenameField(
            model_name="captureanimenamemodel",
            old_name="episdoes",
            new_name="episodes",
        ),
    ]