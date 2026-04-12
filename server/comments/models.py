

# Create your models here.
from django.db import models
from django.conf import settings
from posts.models import Post

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)