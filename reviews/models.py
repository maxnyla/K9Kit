from django.db import models
from profiles.models import UserProfile


class Review(models.Model):
    """
    Model for logged in users to review their shopping experience with the site
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='user_review')
    review_title = models.CharField(max_length=254)
    review_body = models.TextField(blank=True, null=True, default='')
    review_by = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.review_title
