from django.urls import path
from .views import TicketListAPI, TicketCreateAPI, TicketUpdateAPI, TicketDeleteAPI

urlpatterns = [
    path('', TicketListAPI.as_view(), name='ticket_list'),
    path('create/', TicketCreateAPI.as_view(), name='ticket_create'),
    path('update/', TicketUpdateAPI.as_view(), name='ticket_update'),
    path('delete/', TicketDeleteAPI.as_view(), name='ticket_delete'),
]