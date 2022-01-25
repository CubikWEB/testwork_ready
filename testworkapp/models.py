from django.db import models
from datetime import datetime


def default_datetime():
    return datetime.now()

class NewsList(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    title = models.CharField('Название', max_length=50)
    desc = models.TextField('Текст статьи')
    date = models.DateField('Дата создания', default=default_datetime())
    img = models.FileField('Изображение',upload_to='media')
    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return self.title

class comment(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    nameArticle = models.ForeignKey(NewsList, on_delete=models.CASCADE, related_name='comments')
    nameUser = models.CharField('Пользователь', max_length=20, default = 'Anonymus')
    Text = models.TextField('Текст коментария')
    date = models.DateField('Дата создания', default=default_datetime())

    def __str__(self):
        return self.Text


class backsaids(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    Text = models.TextField('Отзыв')
    Email = models.EmailField()
    date = models.DateField('Дата создания', default=default_datetime())

    def __str__(self):
        return self.Text

