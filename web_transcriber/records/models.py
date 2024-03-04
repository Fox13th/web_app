from django.db import models


class Records(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Запись: {self.title}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
