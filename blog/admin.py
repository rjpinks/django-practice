from django.contrib import admin

from .models import Post


class BlogPostAdmin(admin.ModelAdmin):
	fields = ['title', 'genre', 'content', 'image_address']


admin.site.register(Post, BlogPostAdmin)
