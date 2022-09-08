from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='news|index'),
    path('category/<slug:slug>/', NewsByCategory.as_view(), name='news|category'),
    # path('<slug:slug>/', ViewNews.as_view(), name='news|single'),
    path('<slug:category_slug>/<slug:news_slug>/', ViewNews.as_view(), name='news|single'),
]