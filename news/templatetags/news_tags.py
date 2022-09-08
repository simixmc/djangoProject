from django import template
from django.db.models import Q, Count

from news.models import Category


register = template.Library()


@register.simple_tag(name='categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/inc/_list_categories.html')
def show_categories():
    return {'categories': Category.objects.annotate(cnt=Count('news', filter=Q(news__is_published=True))).filter(cnt__gt=0)}
