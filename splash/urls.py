from django.urls import path

from . import views


urlpatterns = [
	# ex: /
	path('', views.index, name='index'),
	# ex: /portfolio
	path('portfolio', views.download_portfolio, name='download_portfolio')
]
