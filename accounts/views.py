from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . auth import unauthenticated_user
# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user_created = User.objects.create_user(username=username, email=email, password=password)
            user_created.save()
            success_msg = 'Registered Successfully'
            messages.success(request, success_msg)
            return redirect('login')
        except Exception as e:
            error_msg = 'Server Unreachable'
            messages.error(request, error_msg)
            return redirect('register')
    return render(request, 'register.html')

@unauthenticated_user
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            error_msg = 'Invalid user'
            messages.error(request, error_msg)
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_(request):
    logout(request)
    msg = 'Logout'
    messages.success(request, msg)
    return redirect('login')