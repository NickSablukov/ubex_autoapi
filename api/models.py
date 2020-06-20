from django.db import models

# Custom testing models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    author = models.ForeignKey("Author", verbose_name="Автор", on_delete=models.CASCADE)
    publish_dt = models.DateField(verbose_name="Дата публикации")

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    is_delicious = models.BooleanField(verbose_name="Вкусная")

    class Meta:
        verbose_name = "пицца"
        verbose_name_plural = "пицца"

    def __str__(self):
        return self.name
