from django.shortcuts import render
from django.views import generic

from posts.models import Post
# Create your views here.
class CreatePost(generic.CreateView):
    model = Post
    fields = ['content']
    template_name = 'createPost.html'
    