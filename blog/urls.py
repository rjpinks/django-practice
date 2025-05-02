from django.urls import path

from . import views


urlpatterns = [
	# ex: /blog/
	path('', views.index, name='index'),
	# ex: /blog/posts
	path('posts/', views.posts_all, name='posts_all'),
	# ex: /blog/posts/art
	path('posts/<slug:genre>', views.posts_genre, name='posts_genre'),
	path('<int:blog_id>', views.post_data, name='post_data')
]
