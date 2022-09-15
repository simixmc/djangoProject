from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import *


class TeaserForm(ModelForm):
    class Meta:
        model = Teaser
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }


class TeaserAdmin(admin.ModelAdmin):
    form = TeaserForm


admin.site.register(Slider)
admin.site.register(Teaser, TeaserAdmin)
