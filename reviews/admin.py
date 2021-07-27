from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'review_title',
        'review_body',
        'review_by',
        'review_date'
    )

    ordering = ('review_title',)

admin.site.register(Review, ReviewAdmin)