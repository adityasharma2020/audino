# Generated by Django 3.2.22 on 2023-10-07 13:14
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0002_auto_20231007_1632"),
    ]

    operations = [
        migrations.CreateModel(
            name="Annotation",
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
                ("cloud_storage_id", models.IntegerField(default=0)),
                ("filename", models.CharField(max_length=500)),
                (
                    "format",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("server", "server"),
                            ("annotation", "annotation"),
                            ("formats", "formats"),
                        ],
                        default="annotation",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("local", "local"),
                            ("cloud_storage", "cloud_storage"),
                        ],
                        default="local",
                        max_length=200,
                        null=True,
                    ),
                ),
                ("use_default_location", models.BooleanField(default=True)),
                ("annotation_file", models.FileField(upload_to="annotations")),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "annotations",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.annotation",
                    ),
                ),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_assignee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "labels",
                    models.ManyToManyField(blank=True, default=None, to="core.Label"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                    ),
                ),
                (
                    "source_storage",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_stg",
                        to="core.storage",
                    ),
                ),
                (
                    "target_storage",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target_stg",
                        to="core.storage",
                    ),
                ),
            ],
        ),
    ]
