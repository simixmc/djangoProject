from django import template

from blog.models import Category


register = template.Library()


@register.inclusion_tag('blog/inc/_list_categories.html')
def show_categories():
    return {'categories': Category.objects.all()}

