from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *


class MainMenuAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(TopBar)
