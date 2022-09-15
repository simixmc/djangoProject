from django import template

from main.models import Slider, Teaser

register = template.Library()


@register.inclusion_tag('main/inc/_slider.html')
def show_slider():
    return {'slider': Slider.objects.all()}


@register.inclusion_tag('main/inc/_teaser.html')
def show_teaser():
    return {'teaser': Teaser.objects.all()}
