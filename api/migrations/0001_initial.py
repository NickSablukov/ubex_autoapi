# Generated by Django 3.0.7 on 2020-06-19 19:58
from typing import List

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
            ],
            options={"verbose_name": "автор", "verbose_name_plural": "авторы"},
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("publish_dt", models.DateField(verbose_name="Дата публикации")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Author",
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={"verbose_name": "книга", "verbose_name_plural": "книги"},
        ),
    ]
