from django.db import models

class Interest(models.Model):
	title = models.CharField(max_length=50, unique=True)
	content = models.TextField()

	def __str__(self):
		return self.title
