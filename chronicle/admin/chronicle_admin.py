from django.contrib import admin

from chronicle import models

from chronicle_inlines import *


class GameAdmin (admin.ModelAdmin):
    list_display = (
        'name', 'enabled', 'chronicle', 'date',
    )
    list_filter = (
        'enabled', 'chronicle', 'date',
    )

admin.site.register(models.Game, GameAdmin)


class ChronicleAdmin (admin.ModelAdmin):
    list_display = (
        'name', 'enabled',
    )
    list_filter = (
        'enabled',
    )
    inlines = [
        GameInline,
    ]

admin.site.register(models.Chronicle, ChronicleAdmin)
