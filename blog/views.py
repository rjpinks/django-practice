from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
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
	if request == 'POST':
		comment = request.POST.get('comment')
		# will need to add account information / autherization here
		Comment.objects.create(comment=comment)
		return redirect(request.path_info)

	blog_post = get_object_or_404(Post, id=blog_id)
	comments = Comment.objects.filter(parent_post=blog_post).order_by('date_pub')[:10]
	return render(request, 'blog/post-data.html', {'post': blog_post, 'comments': comments})


def load_comments(request, blog_id, comment_count):
	total_comments = Comment.objects.filter(parent_post=blog_id).count()
	if comment_count >= total_comments:
		raise Http404('end of comments')

	end_slice = comment_count + 10 if comment_count + 10 <= total_comments else total_comments
	comments = Comment.objects.select_related('author')\
		.filter(parent_post=blog_id)\
		.order_by('-date_pub')\
		.values('id', 'content', 'date_pub', 'author__display_name')[comment_count:end_slice]
	
	return JsonResponse(list(comments), safe=False)


def comment_form(request, blog_id):
	return render(request, 'blog/comment-form.html')


def register(request):
	return render(request, 'blog/registery-form.html')
