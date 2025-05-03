from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator

from .models import Post


def index(request):
	post_genres = Post.objects.values('genre').distinct()
	return render(request, 'blog/index.html', {'posts': post_genres})


def posts_genre(request, genre):
	if genre == 'all':
		posts = Post.objects.all().values('id', 'title', 'date_pub').order_by('-date_pub')
		paginator = Paginator(posts, 10)

		page_num = request.GET.get('page')
		page_obj = paginator.get_page(page_num)
		return render(request, 'blog/posts.html', {'post_paginator': page_obj})

	genre_list = Post.objects.values_list('genre', flat=True).distinct()
	if genre in genre_list:
		posts = Post.objects.filter(genre=genre).values('id', 'title', 'date_pub').order_by('-date_pub')
		paginator = Paginator(posts, 10)

		page_num = request.GET.get('page')
		page_obj = paginator.get_page(page_num)
		return render(request, 'blog/posts.html', {'post_paginator': page_obj})
	
	raise Http404("Genre Not Found")
	

def post_data(request, blog_id):
	blog = Post.objects.filter(id=blog_id)
	if len(blog) != 1:
		raise Http404("Post not found")

	return render(request, 'blog/post-data.html', {'post': blog[0]})
