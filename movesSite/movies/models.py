from django.db import models
from movesSite.models import BaseModel


class Movie(BaseModel):
    title = models.CharField(verbose_name='Название')
    director = models.CharField(verbose_name='Режиссёр')
    genre = models.CharField(blank=True, verbose_name='Жанр')
    releaseYear = models.IntegerField(verbose_name='Год выхода')
    poster = models.ImageField(
        blank=True,
        upload_to='movies_images',
        verbose_name='Постер')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title
