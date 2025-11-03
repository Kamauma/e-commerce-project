from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Register (Signup)
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'accounts/register.html')


# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
