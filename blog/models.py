from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, null=True, verbose_name='URL')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def get_absolute_url(self):
        url = get_parent_path(self)
        return url


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, null=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = TreeForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория', related_name='blog')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-created_at']

    def get_absolute_url(self):
        url = get_parent_path(self.category)
        url += self.slug
        return url


def get_parent_path(item):
    parent = reverse('blog|index')
    length = len(parent)
    parent = parent[:length - 1]
    url = "/%s/" % item.slug
    page = item
    while page.parent:
        url = "/%s%s" % (page.parent.slug, url)
        page = page.parent
    url = parent + url
    return url
