from rest_framework import serializers
from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags"]


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "category",
            "tags",
            "createdAt",
            "updatedAt",
        ]


class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "category",
            "tags",
            "createdAt",
            "updatedAt",
        ]
