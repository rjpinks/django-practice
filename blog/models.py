from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=50, unique=True)
	genre = models.CharField(max_length=50)
	content = models.TextField(blank=True, null=True)
	image_address = models.CharField(max_length=255, blank=True, null=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	last_edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar_address = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.email


class Comment(models.Model):
	content = models.CharField()
	date_pub = models.DateTimeField(auto_now_add=True)

	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
	parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # the related_name should allow reverse look-ups

	def __str__(self):
		return self.content[:10]
