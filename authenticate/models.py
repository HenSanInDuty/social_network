from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    friend = models.ManyToManyField("self",null=True,blank=True)
    fullname = models.CharField(max_length=100)
    avatar = models.TextField()
    user = models.ForeignKey(
        User,
        primary_key = True,
        on_delete=models.CASCADE
    )

