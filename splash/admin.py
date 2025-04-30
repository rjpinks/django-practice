from django.contrib import admin

from .models import Interest, Guestbook

class InterestAdmin(admin.ModelAdmin):
	fields = ['title', 'content']


class GuestbookAdmin(admin.ModelAdmin):
	fields = ['name', 'location', 'comment']


admin.site.register(Interest, InterestAdmin)
admin.site.register(Guestbook, GuestbookAdmin)
