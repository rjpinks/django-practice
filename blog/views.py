from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator

from .models import Post, Comment


def index(request):
	post_genres = Post.objects.values('genre').distinct()
	return render(request, 'blog/index.html', {'posts': post_genres})


def posts_genre(request, genre):
	if genre == 'All':
		posts = Post.objects.all().values('id', 'title', 'date_pub').order_by('-date_pub')
		paginator = Paginator(posts, 10)

		page_num = request.GET.get('page')
		page_obj = paginator.get_page(page_num)
		return render(request, 'blog/posts.html', {'post_paginator': page_obj, 'genre': genre})

	if Post.objects.filter(genre=genre).exists():
		posts = Post.objects.filter(genre=genre).values('id', 'title', 'date_pub').order_by('-date_pub')
		paginator = Paginator(posts, 10)

		page_num = request.GET.get('page')
		page_obj = paginator.get_page(page_num)
		return render(request, 'blog/posts.html', {'post_paginator': page_obj, 'genre': genre})
	
	raise Http404("Genre Not Found")
	

def post_data(request, blog_id):
	blog_post = get_object_or_404(Post, id=blog_id)
	comments = Comment.objects.filter(parent_post=blog_post)
	return render(request, 'blog/post-data.html', {'post': blog_post, 'comments': comments})
