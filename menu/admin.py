from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *


class MainMenuAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'path', 'sort')
    list_editable = ('sort',)
    mptt_level_indent = 20


class TopBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'sort')
    list_editable = ('sort',)


admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(TopBar, TopBarAdmin)
