from django.contrib import admin

from app.models import *


@admin.register(ImageUpload)
class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'file_name', 'letters', 'count', 'created_at', 'updated_at']
    search_fields = ['file_name']
    list_display_links = ['pk', 'file_name']
    date_hierarchy = 'created_at'
