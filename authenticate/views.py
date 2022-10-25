from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from authenticate.forms import CustomUserCreationForm

def dashboard(request):
    return render(request, "auth/dashboard.html")

def register(request):
    print(request.method)
    if request.method == "GET":
        return render(
            request, "auth/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("post")
            return render(request, "auth/login.html")
        else:
            return render(request, "auth/register.html",{"form": form})