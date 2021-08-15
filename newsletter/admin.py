from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'newsletter_title',
        'newsletter_body',
        'newsletter_by',
        'newsletter_date'
    )

    ordering = ('newsletter_date',)

admin.site.register(Newsletter, NewsletterAdmin)
