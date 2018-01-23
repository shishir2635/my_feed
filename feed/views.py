from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from .models import profile,board,like
from .forms import boardform,profileform
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def Index(request):
	post = board.objects.all().count()
	return HttpResponse("No. of post in the system : {} posts".format(post))

# @method_decorator(login_required, name='dispatch')
# class PostListView(generic.ListView):
# 	model = board
# 	paginate_by = 10

def posts_all(request):
	post = board.objects.all().order_by('-time') 
	return render(request,'feed/post_all.html',{'post':post,'numlike':likes,})

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
def profile(request):
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
		posty = board.objects.filter(user=user)
		number = posty.count()
		return render(request,'feed/profilefilled.html',{'posts':posty, 'num':number ,})


