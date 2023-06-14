from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import UsefulLinksModel
from .serializers import UsefulLinksSerializer, UsefulLinkCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CreateUsefulLinksPermission, IsOwner


class ListUsefulLinksAPI(ListAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer
    permission_classes = [IsAuthenticated]


class CreateUsefulLinksAPI(CreateAPIView):
    queryset = UsefulLinksModel.objects.all()
    permission_classes = [IsAuthenticated, CreateUsefulLinksPermission]
    serializer_class = UsefulLinkCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateUsefulLinkAPI(RetrieveUpdateAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinkCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]


class DeleteUsefulLinkAPI(DestroyAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]
