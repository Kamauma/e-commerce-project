from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home page
def home(request):
    return render(request, 'accounts/home.html')

# Login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with that email exists
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'Invalid email or password'})

        # Authenticate using the username found by email
        user = authenticate(request, username=user_obj.username, password=password)

        if user:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid email or password'})

    return render(request, 'accounts/login.html')

# Signup
def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validations
        if password1 != password2:
            return render(request, "accounts/signup.html", {"error": "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {"error": "Username already exists."})

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/signup.html", {"error": "Email already exists."})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "accounts/signup.html")

# Product list (category page)
def product_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/product.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
