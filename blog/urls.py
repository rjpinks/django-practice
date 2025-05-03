from django.urls import path

from . import views


urlpatterns = [
	# ex: /blog/
	path('', views.index, name='index'),
	# ex: /blog/posts/art
	path('posts/<str:genre>', views.posts_genre, name='posts_genre'),
	# ex: /blog/4
	path('<int:blog_id>', views.post_data, name='post_data')
]
