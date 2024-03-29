# Generated by Django 4.0.2 on 2022-02-18 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Control",
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
                ("name", models.CharField(max_length=30, unique=True)),
                ("cid", models.CharField(max_length=10, unique=True)),
                (
                    "ctype",
                    models.CharField(
                        choices=[
                            ("Primary", "Primary"),
                            ("Secondary", "Secondary"),
                            ("Tertiary", "Tertiary"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "last_update",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
