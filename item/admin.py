from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category_id', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    prepopulated_fields = {"slug": ("title",)}

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Item, ItemAdmin)
admin.site.register(Todo, TodoAdmin)
