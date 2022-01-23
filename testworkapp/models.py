from django.db import models
from datetime import datetime


def default_datetime():
    return datetime.now()

class NewsList(models.Model):
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'

    title = models.CharField('Название', max_length=50)
    desc = models.TextField('Текст статьи')
    date = models.DateField('Дата создания', default=default_datetime())
    img = models.FileField('Изображение',upload_to='media')
    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return self.title




