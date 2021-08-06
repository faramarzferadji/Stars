from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'family_name', 'period_play', 'description']


admin.site.register(Player,PlayerAdmin)



