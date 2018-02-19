from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic
from .models import profile,board,comment
from .forms import boardform,profileform,commentform
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

def Index(request):
	return render(request,'feed/home_page.html')

# # @method_decorator(login_required, name='dispatch')
# class PostAll(generic.ListView):
# 	model = board
# 	paginate_by = 10

@login_required(login_url='/login')
def posts_all(request):
	post = board.objects.all().order_by('-time')
	return render(request,'feed/post_all.html',{'post':post,})

@login_required(login_url='/login')
def post_new(request):
    if request.method == "POST":
        form = boardform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= request.user
            post.save()
            return redirect('posts_all')
    else:
        form = boardform()

    return render(request, 'feed/post_new.html', {'form': form})


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('Index')
	else:
		form = UserCreationForm()

	return render(request,'feed/signup.html', {'form':form})

@login_required(login_url='/login')
def profilef(request):
	try:
		shishir = request.user.profile

	except:
		if request.method == 'POST':
			form = profileform(request.POST)
			if form.is_valid():
				profile = form.save(commit=False)
				profile.username = request.user
				profile.save()

				return redirect('Index')

		else:
			form = profileform()

		return render(request,'feed/profile.html',{'form':form})

	else:
		user = request.user
		#name = profile.objects.filter(username=user.get_username)
		profile = request.user.profile
		posty = board.objects.filter(user=user)
		number = posty.count()
		return render(request,'feed/profilefilled.html',{'posts':posty, 'num':number , 'profile':profile,})

@login_required(login_url='/login')
def post_detail(request,pk):
	if request.method == "POST":
		form = commentform(request.POST)
		if form.is_valid():
			com = form.save(commit=False)
			com.comment = form.cleaned_data.get('comment')
			com.user = request.user
			com.post = board(pk=pk)
			com.save()

			return redirect('/feed/post/{}'.format(pk))
	else:
		form = commentform()
		post_ob = board.objects.filter(pk=pk)
		comme = comment.objects.all()
		return render(request,'feed/board_detail.html',{'post':post_ob,'comment':comme,'form':form,})

@login_required(login_url='/login')
def profile_edit(request):
	return HttpResponse('Work in Progress !')

@login_required(login_url='/login')
def like_command(request,pk):
	post = board.objects.get(pk=pk)
	post.likes += 1
	post.save()
	return redirect('posts_all')

@login_required(login_url='/login')  #not in work still
def unlike_command(request,pk):
	post = board.objects.get(pk=pk)
	post.likes -= 1
	post.save()

	return redirect('posts_all')

