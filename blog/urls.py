from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='blog|index'),
    path('<path:full_slug>/', get_category, name='blog|category'),
    path('<path:full_slug>/<slug:slug>', get_single_page, name='blog|single'),
]