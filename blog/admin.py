from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
	fields = ['title', 'genre', 'content', 'image_address']


admin.site.register(BlogPost, BlogPostAdmin)
