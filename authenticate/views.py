from http import HTTPStatus
from django.http import HttpResponse
from django.http import Http404
from email.policy import default
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from authenticate.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from posts.forms import CreatePostForm
from posts.models import Attachment, Post

from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

import json

from authenticate.models import Profile

default_avatar = ""

def dashboard(request):
    return render(request, "auth/dashboard.html")

def register(request):
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

    context = {
    'profiles': Profile.objects.all(),
  }

    if request.user.is_authenticated:
        return render(request,'posts/listPost.html',context)

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
                return render(request,'posts/listPost.html',context)
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'auth/login.html', {'form': form}) 
    

def logout_view(request):
    logout(request)
    return render(request, 'auth/login.html', {'form': AuthenticationForm}) 

def upload_image(image):
    config = cloudinary.config(secure=True)
    c = cloudinary.uploader.upload_image(image)
    return c.url

def profile_update(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.filter(user=user)
        fullname = request.POST['fullname']
        avatar = request.FILES.get('avatar')
        if fullname:
            profile.update(fullname=fullname)
        if avatar and 'image' in avatar.content_type:
            profile.update(avatar=upload_image(avatar))
    return redirect('/profile/'+str(request.user.id))

def delete_post(request):
    prev_url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        id_post = request.POST.get('delete-id')
        Post.objects.filter(pk=id_post).delete()
    return redirect(prev_url)

def like_post(request,id_post):
    if request.method == "POST":
        user = request.user.profile_set.first()
        post = Post.objects.filter(pk=id_post).first()
        if user not in post.liker.all():
            print('ok')
            post.liker.add(user)
        else:
            post.liker.remove(user)
        return HttpResponse(status = 200)
    return HttpResponse(status = 404)

class ProfileDetail(LoginRequiredMixin,generic.ListView):
    login_url = '/signin/'
    template_name = 'auth/profileDetail.html'
    paginate_by = 10
    
    def get_queryset(self):
        #Get user in profile
        user = User.objects.filter(id = self.kwargs.get('id')).first()
        list_post = Post.objects.filter(user=user).order_by('-date')
        return list_post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm
        user = User.objects.filter(id = self.kwargs.get('id')).first()
        if user:
            context['userProfile'] = user.profile_set.first()
            return context
        else:
            raise Http404(("Not found this user"))
        
    def post(self,request,**kwargs):
        images = request.FILES.getlist('image-post')
        form = CreatePostForm(request.POST)
        url = self.request.get_full_path()
        if not form.is_valid():
            return redirect(url)
        post = form.save(user=self.request.user)
        count = 0
        if images:
            for i in images:
                if 'image' not in i.content_type:
                    continue
                if count == 4:
                    break
                url_image = upload_image(i)
                Attachment.objects.create(post=post,
                                          type=0,
                                          url=url_image)
                count+=1
        return redirect(url)