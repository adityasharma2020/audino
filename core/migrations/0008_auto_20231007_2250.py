# Generated by Django 3.2.22 on 2023-10-07 17:20
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_auto_20231007_2211"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="annotations",
        ),
        migrations.AddField(
            model_name="task",
            name="annotations",
            field=models.ManyToManyField(
                blank=True, default=None, to="core.Annotation"
            ),
        ),
    ]
