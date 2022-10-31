from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    friend = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    fullname = models.CharField(max_length=100)
    avatar = models.TextField()