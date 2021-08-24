from django.contrib import admin
from .models import Tip


class TipAdmin(admin.ModelAdmin):
    list_display = (
        'tip_title',
        'tip_body',
        'tip_by',
        'tip_date'
    )

    ordering = ('tip_date',)

admin.site.register(Tip, TipAdmin)