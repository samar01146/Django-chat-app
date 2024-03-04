from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def errors(list_arr):
    for string in list_arr:
        message = f"Please provide appropriate {string}"
        return message
    

# Home page
@login_required(login_url='/auth/login/')
def home(request):
    if request.user != None:
        return render(request, 'home.html')

# signup page
def user_signup(request):
    message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        keys = ['username' , 'password', "confirm_password"]
        message = errors(keys)
        form_data = {"username":username, "password1":password, "password2":confirm_password}
        form = SignupForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {"message":message})

# login page
def user_login(request):
    message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        keys = ['username', 'password']
        message = errors(keys)
        login_data = {"username":username, "password":password}
        form = LoginForm(login_data)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
            else:
                message = "Authentication Failed For Logged User"
    return render(request, 'login.html', {"message":message})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')