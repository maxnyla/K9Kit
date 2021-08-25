from django.contrib import admin
from .models import Tip


class TipAdmin(admin.ModelAdmin):
    list_display = (
        'tip_title',
        'tip_body',
        'tip_by',
    )

    ordering = ('tip_title',)

admin.site.register(Tip, TipAdmin)