from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from authenticate.models import Profile

from posts.models import Post
from posts.forms import CreatePostForm
# Create your views here.
class CreatePost(LoginRequiredMixin,generic.ListView):
    login_url = '/signin/'
    template_name = 'posts/listPost.html'
    paginate_by = 10
    
    def get_queryset(self):
        return ['1','2','3']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm(use_required_attribute=False)
        context['non'] = ["https://img5.thuthuatphanmem.vn/uploads/2021/08/25/hinh-nen-3d-cho-may-tinh-4k_084701936.jpg"]
        cur_id = self.request.GET.get('cur_user')

        context['profiles'] = Profile.objects.all().exclude(user__pk=self.request.user.pk).exclude(user__profile__friend__isnull=False)
        
        return context

    def post(self, request):
        if self.request.POST.get("action") == "add_friend":
           
            cur_id = self.request.POST.get("cur_id")
            friend_id = self.request.POST.get("friend_id")
            curProfile = Profile.objects.filter(pk=cur_id)
            friendProfile = Profile.objects.filter(pk=friend_id).first()

            curProfile.first().friend.add(friendProfile)
            print(friend_id)
            print(curProfile)

            return redirect("/posts")
        if self.request.POST.get("action") == "remove_friend":
            cur_id = self.request.POST.get("cur_id")
            friend_id = self.request.POST.get("friend_id")
            curProfile = Profile.objects.filter(pk=cur_id)
            friendProfile = Profile.objects.filter(pk=friend_id).first()

            curProfile.first().friend.remove(friendProfile)

            print(friend_id)
            print(curProfile)
            return redirect("/posts")
        else:
            return redirect("/signin")