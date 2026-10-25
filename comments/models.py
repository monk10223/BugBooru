from django.db import models

from posts.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    author = models.CharField(max_length=40, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
