from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):

	username = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=100,help_text='full name')
	branch = models.CharField(max_length=10,help_text='Enter your branch initials i.e.. CE for civil engineering')
	year = models.CharField(max_length=10,help_text='Enter your year of study ie.. 2 for 2nd year etc.')
	email = models.EmailField(null=True,help_text='Can be left blank!')

	def __str__(self):
		return self.name

class board(models.Model):

	post = models.CharField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	hash_tags = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.post

# class like(models.Model):

# 	user = models.ForeignKey(User,on_delete=models.CASCADE)
# 	post = models.ForeignKey(board,on_delete=models.CASCADE)

# 	def __str__(self):

# 		return str(self.id)

class comment(models.Model):
	comment = models.CharField(max_length=200)
	post = models.ForeignKey(board,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment