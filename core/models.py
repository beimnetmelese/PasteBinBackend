from django.db import models
from django.utils import timezone
import uuid

class Snippet(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    content_encrypted = models.TextField()
    language = models.CharField(max_length=30, default="plaintext")

    # Password protection
    password_hash = models.CharField(max_length=128, null=True, blank=True)

    # Expiry
    expiry_time = models.DateTimeField(null=True, blank=True)
    one_time_view = models.BooleanField(default=False)
    has_been_viewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        if self.expiry_time and timezone.now() > self.expiry_time:
            return True
        return False
