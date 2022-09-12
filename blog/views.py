from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import *


def index(request):
    blog = Blog.objects.filter(is_published=True).select_related('category')
    paginator = Paginator(blog, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    breadcrumb = get_breadcrumb('')
    context = {
        'title_page': 'Статьи',
        'page_obj': page_obj,
        'breadcrumb': breadcrumb,
    }
    return render(request=request, template_name='blog/index.html', context=context)


def get_category(request, full_slug):
    category_id = get_parent(full_slug)
    category = Category.objects.get(pk=category_id)
    blog = Blog.objects.filter(is_published=True, category=category).select_related('category')
    paginator = Paginator(blog, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    breadcrumb = get_breadcrumb(full_slug=full_slug)
    context = {
        'title_page': category.title,
        'page_obj': page_obj,
        'breadcrumb': breadcrumb,
    }
    return render(request=request, template_name='blog/index.html', context=context)


def get_single_page(request, full_slug, slug):
    category = get_parent(full_slug)
    breadcrumb = get_breadcrumb(full_slug=full_slug)
    context = {
        'title_page': 'Статьи',
        'item': Blog.objects.get(is_published=True, slug=slug, category=category),
        'breadcrumb': breadcrumb,
    }
    return render(request=request, template_name='blog/single.html', context=context)


def get_breadcrumb(full_slug):
    breadcrumb = [{
        'title': 'Статьи',
        'url': reverse('blog|index')
    }]
    if full_slug != '':
        path = full_slug.split('/')
        for item in path:
            data = {
                'title': Category.objects.get(slug=item).title,
                'url': Category.objects.get(slug=item).get_absolute_url()
            }
            breadcrumb.append(data)
    return breadcrumb


def get_parent(full_slug):
    path = full_slug.split('/')
    parent = 0
    for slug in path:
        if parent == 0:
            category = Category.objects.filter(parent__isnull=True).get(slug=slug)
        else:
            category = Category.objects.get(slug=slug, parent=parent)
        parent = category.pk
    return parent
