from django.contrib import admin

from models import Key

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('public', 'private')
    list_display_links = None
    list_editable = ('public', 'private')
