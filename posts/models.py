from django.db import models

from posts.validators import validate_image_url


# Create your models here.
class Post(models.Model):
    image_url = models.URLField(validators=[validate_image_url])
    uploaded_by = models.CharField(max_length=40, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('tags.Tag', blank=True, null=True, related_name="posts")