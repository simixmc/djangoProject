from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'updated_at', 'get_photo', 'slug', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    # fields = ('category', 'title', 'slug', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at')
    fieldsets = [
        ('Основные настройки', {
            'fields': ['category', 'title', 'slug', 'is_published'],
        }),
        ('Контент', {
            'fields': ['content', 'photo', 'get_photo'],
        }),
    ]
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Изображение'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
