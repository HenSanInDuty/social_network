from django.shortcuts import render
from django.views import generic

from posts.models import Post
from posts.forms import CreatePostForm
# Create your views here.
class CreatePost(generic.ListView):
    template_name = 'createPost.html'
    paginate_by = 10
    
    def get_queryset(self) :
        return ['1','2','3']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm(use_required_attribute=False)
        context['non'] = "non"
        return context