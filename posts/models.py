from django.db import models

# Create your models here.
class Post(models.Model):
    image_url = models.URLField()
    description = models.TextField(max_length= 300, blank=True, null=True)
    uploaded_by = models.CharField(max_length=40, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('tags.Tag', blank=True, null=True, related_name="posts")