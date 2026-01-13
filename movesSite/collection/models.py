from django.db import models
from movesSite.models import BaseModel


class Collection(BaseModel):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    movies = models.ManyToManyField(
        'movies.Movie', 
        related_name='collections',  
        verbose_name="Фильмы"
    )

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name
