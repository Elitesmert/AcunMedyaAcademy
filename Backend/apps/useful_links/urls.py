from django.urls import path
from .views import ListUsefulLinksAPI, CreateUsefulLinksAPI

urlpatterns = [
    path('', ListUsefulLinksAPI.as_view(), name='useful_links_list'),
    path('add/', CreateUsefulLinksAPI.as_view(), name='useful_links_create'),
]
