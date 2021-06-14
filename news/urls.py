from django.urls import path
from django.conf.urls.static import static
from .views import (
    ListCategoryAPIView,
    DetailCategoryAPIView,
    PostListAPIView,
    PostDetailAPIView,
    CommentsAPIView,
    UpvoteAPIView,
)
from KyivTest import settings

urlpatterns = [
    path("categories/", ListCategoryAPIView.as_view(), name="categories-list"),
    path(
        "categories/<int:pk>/",
        DetailCategoryAPIView.as_view(),
        name="categories-detail",
    ),
    path("posts/", PostListAPIView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("comments/", CommentsAPIView.as_view(), name="commentslilst"),
    path("upvote/", UpvoteAPIView.as_view(), name="upvote"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
