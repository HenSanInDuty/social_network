from cProfile import label
from django import forms
from .models import Post
class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['content']
        label = {
            'content':"Content"
        }
        widgets = {
            'content':forms.Textarea(attrs={'placeholder':'What in your mind ? Can you share this for everyone :3'})
        }