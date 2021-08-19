from django.db import models
from profiles.models import UserProfile


class Newsletter(models.Model):
    """
    Model for site owners to post periodic newsletters
    """
    newsletter_title = models.CharField(max_length=254)
    newsletter_body = models.TextField(blank=True, null=True, default='')
    newsletter_by = models.CharField(max_length=254, default='')
    newsletter_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-newsletter_date']

    def __str__(self):
        return self.newsletter_title