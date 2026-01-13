from django.db import models
from movesSite.models import BaseModel


class Review(BaseModel):
    userId = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="Пользователь")
    content = models.TextField(verbose_name='Контент')
    rating = models.IntegerField(verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def getReview(self, movieId: str):
        pass
