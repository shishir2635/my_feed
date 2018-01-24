from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('',views.Index,name='Index'),
	path('post/',views.posts_all,name='posts_all'),
	path('post/add/',views.post_new, name='newpost'),
	path('post/<pk>/',views.post_detail,name='post_detail'),
	path('post/<pk>/like',views.like_command,name='like_command'),
	#path('post/<pk>/comment',views.post_comment,name='post_comment'),
	#path('trending/',views.trending,name='trending')
]