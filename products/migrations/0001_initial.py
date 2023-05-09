# Generated by Django 4.1.1 on 2023-03-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="number",
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
                ("no", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="prod",
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
                ("img", models.TextField()),
                ("title", models.TextField()),
                ("disc", models.TextField()),
                ("price", models.IntegerField()),
            ],
        ),
    ]
