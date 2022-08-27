from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Login views here.
def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Login Sucessfull"))
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("Invalid Username or Password"))
            return redirect('login')
    else:
        return render (request, 'auth/login.html', {})
# Logout views here.      
def logout_auth(request):
    logout(request)
    messages.success(request, ("Logged out successfully!"))
    return redirect('home')
        
# signup views here.      
def signup_auth(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration was Succefull your username is " + username))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render (request, 'auth/signup.html', {'form':form})