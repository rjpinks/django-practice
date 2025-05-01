from django.shortcuts import render

from .models import Post


def index(request):
	post_genres = Post.objects.values('genre').distinct()
	return render(request, 'blog/index.html', {'posts': post_genres})


def posts_genre(request, genre):
	if genre == 'all':
		posts = Post.objects.all().values('title', 'date_pub').order_by('-date_pub')
		return render(request, 'blog/posts.html', {'posts': posts})

	genre_list = Post.objects.values_list('genre', flat=True).distinct()
	if genre in genre_list:
		posts = Post.objects.filter(genre=genre).values('title', 'date_pub').order_by('-date_pub')
		return render(request, 'blog/posts.html', {'posts': posts})
	
	return Http404("Genre Not Found")
	