from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import Http404
from django.contrib.auth.models import User
from authenticate.models import Profile
from authenticate.views import upload_image

from posts.models import Attachment, Post
from posts.forms import CreatePostForm
# Create your views here.
class CreatePost(LoginRequiredMixin,generic.ListView):
    login_url = '/signin/'
    template_name = 'posts/listPost.html'
    paginate_by = 10
    
    def get_queryset(self):
        user = self.request.user
        list_post = Post.objects.all().order_by('-date')
        list_post =  list_post.filter(user__profile__in = user.profile_set.first().friend.all())
        list_post |= Post.objects.filter(user__pk=user.pk)
        #Nom Nom 1 Nom
        return list_post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['form'] = CreatePostForm(use_required_attribute=False)
        context['profiles'] = Profile.objects.all().exclude(user__pk=user.pk).exclude(user__profile__in = user.profile_set.first().friend.all())
        
        return context

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
                post.liker.add(user)
            else:
                post.liker.remove(user)
            return HTTPResponse(status = 200)
        return SMTPResponseException(status = 404)

    def post(self, request):
        if self.request.POST.get("action") == "add_friend":
           
            cur_id = self.request.POST.get("cur_id")
            friend_id = self.request.POST.get("friend_id")
            curProfile = Profile.objects.filter(pk=cur_id)
            friendProfile = Profile.objects.filter(pk=friend_id).first()
            curProfile.first().friend.add(friendProfile)
            return redirect("/posts")
        if self.request.POST.get("action") == "remove_friend":
            cur_id = self.request.POST.get("cur_id")
            friend_id = self.request.POST.get("friend_id")
            curProfile = Profile.objects.filter(pk=cur_id)
            friendProfile = Profile.objects.filter(pk=friend_id).first()
            curProfile.first().friend.remove(friendProfile)
            return redirect("/posts")

        if self.request.POST.get("action") == "post":
            print('post')
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