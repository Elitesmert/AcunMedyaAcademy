from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import UsefulLinksModel
from .serializers import UsefulLinksSerializer


class ListUsefulLinksAPI(ListAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer


class CreateUsefulLinksAPI(CreateAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
