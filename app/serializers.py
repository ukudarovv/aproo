from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'content')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'reviews', 'publish_date')

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        instance.author = author
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
