from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):

	username = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	branch = models.CharField(max_length=10)
	year = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class board(models.Model):

	post = models.CharField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	hash_tags = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.hash_tags

# class like(models.Model):

# 	user = models.ForeignKey(User,on_delete=models.CASCADE)
# 	post = models.ForeignKey(board,on_delete=models.CASCADE)

# 	def __str__(self):

# 		return str(self.id)
