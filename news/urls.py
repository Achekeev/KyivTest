from django.urls import path
from django.conf.urls.static import static
from .views import (
    ListCategoryAPIView,
    DetailCategoryAPIView,
    PostListAPIView,
    PostDetailAPIView,
    CommentsAPIView,
    UpvoteAPIView,
    CommentsDetailAPIView, SubscribeAPIView,
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
    path(
        "comments/<int:pk>/", CommentsDetailAPIView.as_view(), name="comments-details"
    ),
    path("upvote/", UpvoteAPIView.as_view(), name="upvote"),
    path("subscribe/", SubscribeAPIView.as_view(), name='subscribers-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
