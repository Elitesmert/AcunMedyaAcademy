from django.urls import path
from .views import (ListUsefulLinksAPI, CreateUsefulLinksAPI, UpdateUsefulLinkAPI, DeleteUsefulLinkAPI,)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 1)(ListUsefulLinksAPI.as_view()), name='useful_links_list'),
    path('add/', CreateUsefulLinksAPI.as_view(), name='useful_links_create'),
    path('update/<pk>/', UpdateUsefulLinkAPI.as_view(), name='useful_links_update'),
    path('delete/<pk>/', DeleteUsefulLinkAPI.as_view(), name='useful_links_delete'),
]
