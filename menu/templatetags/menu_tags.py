from django import template

from menu.models import *


register = template.Library()


@register.inclusion_tag('inc/header/inc/_menu_desktop.html')
def show_main_menu():
    return {'main_menu': MainMenu.objects.all()}


@register.inclusion_tag('inc/header/inc/_topbar.html')
def show_topbar():
    return {'topbar': TopBar.objects.all()}


@register.inclusion_tag('inc/header/inc/_topbar_mobile.html')
def show_topbar_mobile():
    return {'topbar_mobile': TopBar.objects.all()}


@register.inclusion_tag('inc/header/inc/_main_menu_mobile.html')
def show_main_menu_mobile():
    return {'main_menu': MainMenu.objects.all()}
