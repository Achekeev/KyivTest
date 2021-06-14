from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Title")
    author = models.CharField(max_length=255, default="Name")
    date_posted = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="~./media")
    image2 = models.ImageField(upload_to="~./media", blank=True, null=True)
    image3 = models.ImageField(upload_to="~./media", blank=True, null=True)
    image4 = models.ImageField(upload_to="~./media", blank=True, null=True)

    class Meta:
        ordering = ("-date_posted",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"


class UpVote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="upvotes")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return self.post
