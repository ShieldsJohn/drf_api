from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class SavedPost(models.Model):
    """
    Model for users to save favourite posts by other users
    """
    owner = models.ForeignKey(User, related_name='saved_posts', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='saved_by', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.owner.username} saved {self.post.title}"
