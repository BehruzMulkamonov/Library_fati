from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import BookSerializer, DiscussSerializer, MagazineSerializer, AbstractSerializer
from books.models import Book, Abstract, Discuss, Magazine


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DiscussAPIViewSet(viewsets.ModelViewSet):
    queryset = Discuss.objects.all()
    serializer_class = DiscussSerializer


class MagazineAPIViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class AbstractAPIViewSet(viewsets.ModelViewSet):
    queryset = Abstract.objects.all()
    serializer_class = AbstractSerializer
