from django.contrib import admin

from .models import Interest

class InterestAdmin(admin.ModelAdmin):
	fields = ['title', 'content']

admin.site.register(Interest, InterestAdmin)
