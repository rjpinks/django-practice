from django.urls import path

from . import views


urlpatterns = [
	# ex: /
	path('', views.index, name='index'),
	# ex: /resume
	path('resume', views.download_resume, name='download_resume'),
	# ex: /contact
	path('contact', views.contact, name='contact'),
	path('guestbook', views.guestbook, name='guestbook'),
	# path('guestbook/submit', views.guestbook_submit, name="guestbook_submit")
]
