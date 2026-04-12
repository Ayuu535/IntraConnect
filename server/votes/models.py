

# Create your models here.
from django.db import models
from django.conf import settings
from IntraConnect.backend.posts.models import Post

User = settings.AUTH_USER_MODEL

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')

    VOTE_TYPE = (
        (1, 'UPVOTE'),
        (-1, 'DOWNVOTE'),
    )
    vote_type = models.SmallIntegerField(choices=VOTE_TYPE)

    class Meta:
        unique_together = ('user', 'post')