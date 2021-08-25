from django.db import models


class Tip(models.Model):
    """ Model for site owners to post periodic tips """
    
    tip_title = models.CharField(max_length=254)
    tip_body = models.TextField(blank=True, null=True, default='')
    tip_by = models.CharField(max_length=254, default='')

    class Meta:
        ordering = ['-tip_title']

    def __str__(self):
        return self.tip_title
