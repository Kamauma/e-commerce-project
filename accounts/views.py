# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product

# Home page
def home(request):
    return render(request, 'accounts/home.html')


# Login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


# Product page
def product_list(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'product': products})


# Signup page
def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Basic validations
        if password1 != password2:
            return render(request, "accounts/signup.html", {"error": "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {"error": "Username already exists."})

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/signup.html", {"error": "Email already exists."})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Redirect to login page after successful signup
        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")  # 'login' should be the name of your login URL pattern

    return render(request, "accounts/signup.html")
