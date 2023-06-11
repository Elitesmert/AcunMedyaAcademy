from django.urls import path
from .views import (ListUsefulLinksAPI, CreateUsefulLinksAPI, UpdateUsefulLinkAPI, DeleteUsefulLinkAPI,)

urlpatterns = [
    path('', ListUsefulLinksAPI.as_view(), name='useful_links_list'),
    path('add/', CreateUsefulLinksAPI.as_view(), name='useful_links_create'),
    path('update/<pk>/', UpdateUsefulLinkAPI.as_view(), name='useful_links_update'),
    path('delete/<pk>/', DeleteUsefulLinkAPI.as_view(), name='useful_links_delete'),
]
