from django.urls import path
from .views import TicketListAPI

urlpatterns = [
    path('', TicketListAPI.as_view(), name='ticket_list'),
]