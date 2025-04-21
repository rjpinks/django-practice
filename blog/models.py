from django.db import models


class BlogPost(models.Model):
	title = models.CharField(max_length=50, unique=True)
	genre = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	image_address = models.CharField(max_length=255, blank=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __str__(self):
		return self.title


class BlogUser(models.Model):
	email = models.EmailField(unique=True)
	display_name = models.CharField(max_length=100)
	blog_pass = models.CharField(min_length=6, max_length=30)
	date_joined = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


class BlogComment(models.Model):
	content = models.CharField()
	date_pub = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now_add=True, auto_now=True)

	author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.content[:10]
