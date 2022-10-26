from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from authenticate.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

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
            
            print("post")
            return render(request, "auth/login.html",{"form": AuthenticationForm})
        else:
            return render(request, "auth/register.html",{"form": form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, "auth/dashboard.html")

    elif request.method == "GET":
        return render(
            request, "auth/login.html",
            {"form": AuthenticationForm}
        )

    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "auth/dashboard.html")
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'auth/login.html', {'form': form}) 
    

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html', {'form': AuthenticationForm}) 