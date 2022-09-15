from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to='banner/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    sub_title = models.CharField(max_length=255, verbose_name='Подзаголовок')
    button_text = models.CharField(max_length=100, blank=True, verbose_name='Текст кнопки')
    button_link = models.CharField(max_length=500, blank=True, verbose_name='Ссылка кнопки')
    sort = models.IntegerField(default=100, verbose_name='Сортировка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'
        ordering = ['sort']


class Teaser(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=100, verbose_name='Описание')
    icon = models.CharField(max_length=20, verbose_name='Иконка')
    color = models.CharField(max_length=20, verbose_name='Цвет', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тизер'
        verbose_name_plural = 'тизеры'
        ordering = ['title']
