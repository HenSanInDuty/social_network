from django.db import models
from django.contrib.auth.models import User

from authenticate.models import Profile
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    liker = models.ManyToManyField(Profile,related_name="like_post")
    
class Attachment(models.Model):
    TYPE_ATTACH = (
        (0,'Image'),
        (1,'Video')
    )
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    type = models.IntegerField(default=0,choices=TYPE_ATTACH)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    