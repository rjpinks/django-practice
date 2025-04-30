from django.urls import path

from . import views


urlpatterns = [
	# ex: /
	path('', views.index, name='index'),
	# ex: /resume
	path('resume', views.download_resume, name='download_resume'),
	# ex: /contact
	path('contact', views.contact, name='contact'),
	# ex: /guestbook POST & GET
	path('guestbook', views.guestbook, name='guestbook'),
	# ex: /portfolio
	path('portfolio', views.portfolio, name='portfolio')
]
