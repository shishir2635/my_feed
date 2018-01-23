from .models import board,profile
from django.forms import ModelForm

class boardform(ModelForm):
	class Meta:
		model = board
		fields = ['post','hash_tags']

class profileform(ModelForm):
	class Meta:
		model = profile
		fields = ['name','branch','year']