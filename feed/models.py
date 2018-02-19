from django.db import models
from django.contrib.auth.models import User

# this will include choices sections
Year_Choices = (
    ('1','1st Year'),
    ('2', '2nd Year'),
    ('3','3rd Year'),
    ('4','4th Year'),
)


Branch_Choices = (
	('CSE' , 'Computer Science And Engineering'),
	('IT' , 'Information Technology'),
	('EC' , 'Electronics Engineering'),
	('EEE' , 'Electrical And Electronics Engineering'),
	('CE','Civil Engineering'),
	('ME' , 'Mechanical Engineering'),
	('EE' , 'Electrical Engineering'),
	('IC' , 'Instrumentation and Control'),
	)
# this ends here



class profile(models.Model):

	username = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=100,help_text='full name')
	branch = models.CharField(max_length=10,choices=Branch_Choices,help_text='Enter your branch initials i.e.. EEE for electrical and electronics engineering')
	year = models.CharField(max_length=10, choices=Year_Choices ,help_text='Enter your year of study ie.. 2 for 2nd year etc.')
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

class comment(models.Model):
	
	comment = models.CharField(max_length=200)
	post = models.ForeignKey(board,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment


# class like(models.Model):
# 	by = models.ForeignKey(User,on_delete=models.CASCADE)
# 	post = models.ForeignKey(board,on_delete=models.CASCADE)

# 	def __str__(self):
# 		return str(self.id)