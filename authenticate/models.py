from django.db import models

class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    avatar = models.TextField()
