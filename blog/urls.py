from django.urls import path

from . import views


urlpatterns = [
	# ex: /blog/
	path('', views.index, name='blog'),
	# ex: /blog/posts/art
	path('posts/<str:genre>', views.posts_genre, name='posts_genre'),
	# ex: /blog/4
	path('<int:blog_id>', views.post_data, name='post_data'),
	# ex: /blog/api/comments/117/10
	path('api/comments/<int:blog_id>/<int:comment_count>', views.load_comments, name='load_comments'),
	# ex: /blog/register
	path('register', views.register, name='register'),
	# ex: /blog/login
	path('login', views.Login.as_view(), name='login'),
	# ex: /blog/logout
	path('logout', views.Logout.as_view(), name='logout'),
	# ex: /blog/api/comment-form
	path('api/comment-form', views.comment_form, name='comment_form'),
]
