from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer, TicketCreateUpdateSerializer


class TicketListAPI(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class TicketCreateAPI(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketUpdateAPI(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


class TicketDeleteAPI(DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
