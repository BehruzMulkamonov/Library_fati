from rest_framework import serializers

from apps.books.models import Book, Discuss, Magazine, Abstract

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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
