from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import UsefulLinksModel
from .serializers import ListUsefulLinksSerializer

class ListUsefulLinksAPI(ListAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = ListUsefulLinksSerializer