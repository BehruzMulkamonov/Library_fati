from rest_framework import serializers

from books.models import Book, Discuss, Magazine, Abstract


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


class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstract
        fields = '__all__'