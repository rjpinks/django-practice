from django.shortcuts import render
from django.http import Http404

from .models import Post


def index(request):
	post_genres = Post.objects.values('genre').distinct()
	return render(request, 'blog/index.html', {'posts': post_genres})


def posts_all(request):
	posts = Post.objects.all().values('id', 'title', 'date_pub').order_by('-date_pub')
	return render(request, 'blog/posts.html', {'posts': posts})


def posts_genre(request, genre):
	genre_list = Post.objects.values_list('genre', flat=True).distinct()
	if genre in genre_list:
		posts = Post.objects.filter(genre=genre).values('id', 'title', 'date_pub').order_by('-date_pub')
		return render(request, 'blog/posts.html', {'posts': posts})
	
	raise Http404("Genre Not Found")
	

def post_data(request, blog_id):
	blog = Post.objects.filter(id=blog_id)
	if len(blog) != 1:
		raise Http404("Post not found")

	return render(request, 'blog/post-data.html', {'post': blog[0]})
