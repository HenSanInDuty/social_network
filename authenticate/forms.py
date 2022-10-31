from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("fullname",)
        
    def save(self, commit = True):
        user = super().save(commit)
        value = {
            'fullname': self.cleaned_data.get('fullname'),
            'avatar': 'https://img.freepik.com/premium-vector/person-avatar-design_24877-38137.jpg?w=2000'
        }
        Profile.objects.create(**value,user = user)
        return user

    