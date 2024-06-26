# Generated by Django 5.0.1 on 2024-04-25 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0004_merge_20240420_1657"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapPin",
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
                ("address", models.CharField(max_length=255)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="map_pins",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
