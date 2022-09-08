from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import News, Category


class HomeNews(ListView):
    paginate_by = 5
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # allow_empty = False
    extra_context = {'title_page': 'Новости'}

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
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return News.objects.filter(category=category.pk, is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/single.html'
    context_object_name = 'item'

    def get_object(self, queryset=None):
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        return News.objects.get(category=category.pk, slug=self.kwargs['news_slug'])
