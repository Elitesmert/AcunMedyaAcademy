from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import UsefulLinksModel
from .serializers import UsefulLinksSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CreateUserfulLinksPermission


class ListUsefulLinksAPI(ListAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer
    permission_classes = [IsAuthenticated]


class CreateUsefulLinksAPI(CreateAPIView):
    queryset = UsefulLinksModel.objects.all()
    permission_classes = [CreateUserfulLinksPermission]
    serializer_class = UsefulLinksSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateUsefulLinkAPI(RetrieveUpdateAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer
    lookup_field = 'pk'


class DeleteUsefulLinkAPI(DestroyAPIView):
    queryset = UsefulLinksModel.objects.all()
    serializer_class = UsefulLinksSerializer
    lookup_field = 'pk'
