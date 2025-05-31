from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, CustomUser


class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'genre', 'content', 'image_address']
    list_display = ['title', 'genre']
    search_fields = ['title', 'genre']


# look into Docs bc I do not understand this code.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'date_of_birth', 'display_name'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'date_of_birth', 'display_name'),
        }),
    )
    list_display = UserAdmin.list_display + ('bio', 'date_of_birth')  # optional, but useful


admin.site.register(Post, BlogPostAdmin)
