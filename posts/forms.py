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
            'content':forms.Textarea()
        }