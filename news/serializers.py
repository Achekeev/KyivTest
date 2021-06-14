from rest_framework import serializers
from .models import NewsCategory, Post, Comment, UpVote, Subscribe
from rest_framework.reverse import reverse


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = (
            "id",
            "name",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "post", "name", "body", "created_at", "is_active")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    upvotes = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
            "title",
            "author",
            "date_posted",
            "link",
            "body",
            "comments",
            "upvotes",
            "image",
            "image2",
            "image3",
            "image4",
        )

    def get_upvotes(self, obj):
        return obj.upvotes.count()

    def get_link(self, obj):
        return "http://localhost:8000" + reverse("post-detail", kwargs={"pk": obj.id})


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = ("id", "post", "like", "dislike")


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ("id", "email")
