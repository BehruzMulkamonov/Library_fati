from rest_framework import serializers

from .models import Book, Discuss, Magazine


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class DiscussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discuss
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'
