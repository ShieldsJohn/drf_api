from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Reaction(models.Model):
    """
    unique_together - ensures a user can't react the same way to the same post twice
    """
    REACTION_TYPES = [
        ('like', 'Like'),
        ('funny', 'Funny'),
        ('sad', 'Sad'),
        ('cute', 'Cute'),
        ('celebrate', 'Celebrate'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='reactions', on_delete=models.CASCADE
    )
    reaction_type = models.CharField(max_length=20, choices=REACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post', 'reaction_type']

    def __str__(self):
        return f'{self.owner} reacted {self.reaction_type} to {self.post}'
