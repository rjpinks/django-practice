from django.urls import path

from . import views


urlpatterns = [
	# ex: /
	path('', views.index, name='index'),
	# ex: /resume
	path('resume', views.download_resume, name='download_resume')
]
