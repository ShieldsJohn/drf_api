from django.db import models

class Contact(models.Model):
    """
    Contact form model
    Provides field for superuser(s) to reply
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    admin_reply = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"From {self.name} || Received: {self.created_at}"
