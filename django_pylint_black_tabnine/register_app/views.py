from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
import hashlib


# Create your views here.
def home(request):
    return render(request, "home.html")


def register(request):
    """"""
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if not (username and password and email):
            return render(
                request, "register.html", {"error": "Please fill in all fields."}
            )

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(
                request, "register.html", {"error": "Username already taken."}
            )

        # Check if the email is already in use
        if User.objects.filter(email=email).exists():
            return render(
                request, "register.html", {"error": "Email already registered."}
            )

        # Create the new user
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        new_user = User.objects.create_user(
            username=username, password=hashed_password, email=email
        )

        # Log in the newly registered user
        django_login(request, new_user)
        print("successfully created new user")
        return redirect(reverse("home"))


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not (username and password):
            return render(request, "login.html", {"error": "Invalid credentials."})

        user = authenticate(
            username=username,
            password=hashlib.sha256(password.encode("utf-8")).hexdigest(),
        )

        if user is not None:
            # User is valid, and login is successful.
            django_login(request, user)
            return redirect(reverse("home"))
        else:
            # Invalid login credentials.
            return render(request, "login.html", {"error": "Invalid credentials."})


def logout(request):
    django_logout(request)
    return redirect(reverse("home"))
