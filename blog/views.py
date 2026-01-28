from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import post
from . import models
def test(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

@login_required
def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def newPost(request):
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    return render(request, 'newpost.html')

@login_required
def myPost(request):
    context ={'posts': post.objects.filter(author = request.user)}
    return render(request, 'mypost.html', context)


def signout(request):
    pass                                                                                                

