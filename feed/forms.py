from .models import board,profile,comment
from django.forms import ModelForm

class boardform(ModelForm):
	class Meta:
		model = board
		fields = ['post','hash_tags']

class profileform(ModelForm):
	class Meta:
		model = profile
		fields = ['name','branch','year','email']

class commentform(ModelForm):
	class Meta:
		model = comment
		fields = ['comment']