from django.contrib import admin
from .models import NewsCategory, Post, Comment, UpVote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "date_posted")
    ordering = ("title",)
    search_fields = ("title", "author")


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "created_at")
    ordering = ("-created_at",)
    search_fields = ("post",)


admin.site.register(NewsCategory)
admin.site.register(UpVote)
