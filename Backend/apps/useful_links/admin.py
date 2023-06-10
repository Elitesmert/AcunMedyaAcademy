from django.contrib import admin
from .models import UsefulLinksModel

@admin.register(UsefulLinksModel)
class UsefulLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'author', 'language')
    search_fields = ('name', 'link', 'author')
