from django.urls import path
from .views import ListUsefulLinksAPI

urlpatterns = [
    path('', ListUsefulLinksAPI.as_view(), name='useful_links_list'),
]
