

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from posts.models import Post

User = settings.AUTH_USER_MODEL

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')

    VOTE_TYPE = (
        (1, 'UPVOTE'),
        (-1, 'DOWNVOTE'),
    )
    vote_type = models.SmallIntegerField(choices=VOTE_TYPE)

    class Meta:
        unique_together = ('user', 'post')


