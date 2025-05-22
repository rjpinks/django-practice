from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
	title = models.CharField(max_length=50, unique=True)
	genre = models.CharField(max_length=50)
	content = models.TextField(blank=True, null=True)
	image_address = models.CharField(max_length=255, blank=True, null=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class User(models.Model):
	email = models.EmailField(unique=True)
	display_name = models.CharField(max_length=100)
	blog_pass = models.CharField(max_length=255)
	date_joined = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


class Comment(models.Model):
	content = models.CharField()
	date_pub = models.DateTimeField(auto_now_add=True)

	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # the related_name should allow reverse look-ups

	def __str__(self):
		return self.content[:10]
