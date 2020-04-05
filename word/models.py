from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
	main_word = models.CharField(max_length=200)
	mean_word = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.main_word} == {self.mean_word}"