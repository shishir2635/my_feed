from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('',views.Index,name='Index'),
	path('post/',views.posts_all,name='posts_all'),
	path('post/add/',views.post_new, name='newpost'),
	#path('trending/',views.trending,name='trending')
]