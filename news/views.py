from .models import NewsCategory, Post, Comment, UpVote, Subscribe
from rest_framework import generics, permissions
from .serializers import (
    CategorySerializer,
    PostSerializer,
    CommentSerializer,
    UpvoteSerializer,
    SubscribeSerializer,
)


class ListCategoryAPIView(generics.ListAPIView):
    queryset = NewsCategory.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = CategorySerializer


class DetailCategoryAPIView(generics.RetrieveAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class CommentsAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteAPIView(generics.ListCreateAPIView):
    queryset = UpVote.objects.all()
    serializer_class = UpvoteSerializer


class SubscribeAPIView(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
