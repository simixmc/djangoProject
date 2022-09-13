from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MainMenu(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    path = models.CharField(max_length=500, null=True, verbose_name='URL')
    sort = models.IntegerField(max_length=15, null=True, verbose_name='Сортировка')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'главное меню'
        verbose_name_plural = 'главное меню'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['sort']


class TopBar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    path = models.CharField(max_length=500, null=True, verbose_name='URL')
    sort = models.IntegerField(max_length=15, null=True, verbose_name='Сортировка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'верхнее меню'
        verbose_name_plural = 'верхнее меню'
        ordering = ['sort']
