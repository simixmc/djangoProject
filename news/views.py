# from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .models import News, Category


def get_breadcrumb(full_slug):
    breadcrumb = [{
        'title': 'Новости',
        'url': reverse_lazy('news|index')
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


class HomeNews(ListView):
    paginate_by = 5
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title_page': 'Новости',
        'breadcrumb': get_breadcrumb(''),
    }

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    paginate_by = 5
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title_page'] = Category.objects.get(slug=self.kwargs['slug'])
        context['breadcrumb'] = get_breadcrumb(Category.objects.get(slug=self.kwargs['slug']).slug)
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return News.objects.filter(category=category.pk, is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/single.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewNews, self).get_context_data(**kwargs)
        context['breadcrumb'] = get_breadcrumb(Category.objects.get(slug=self.kwargs['category_slug']).slug)
        return context

    def get_object(self, queryset=None):
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        return News.objects.get(category=category.pk, slug=self.kwargs['news_slug'])
