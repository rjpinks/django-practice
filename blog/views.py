from django.shortcuts import render

from .models import Post


def index(request):
	post_genres = Post.objects.values('genre').distinct()
	return render(request, 'blog/index.html', {'posts': post_genres})


def posts(request):
	posts = Post.objects.all()
	return render(request, 'blog/posts.html', {'posts': posts})


def posts_genre(request):
	posts = Post.objects.filter(genre=request.genre)
	return render(request, 'blog/posts.html', {'posts': posts})
	