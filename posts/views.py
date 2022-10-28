from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from posts.models import Post
from posts.forms import CreatePostForm
# Create your views here.
class CreatePost(LoginRequiredMixin,generic.ListView):
    login_url = '/signin/'
    template_name = 'listPost.html'
    paginate_by = 10
    
    def get_queryset(self) :
        return ['1','2','3']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm(use_required_attribute=False)
        context['non'] = ["https://img5.thuthuatphanmem.vn/uploads/2021/08/25/hinh-nen-3d-cho-may-tinh-4k_084701936.jpg"]
        return context