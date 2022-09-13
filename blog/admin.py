from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import *


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'updated_at', 'slug', 'is_published',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
