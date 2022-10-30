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
            'content':forms.Textarea(attrs={'placeholder':'What in your mind ? Can you share this for everyone :3','class':'rounded-4 p-2'})
        }
    
    def is_valid(self):
        if self.data['content'] is not None:
            return True
        return super().is_valid()
    
    def save(self, commit = True , **kwargs):
        if commit:
            p = Post.objects.create(user=kwargs.get('user'),
                                    content=self.data['content'])
            return p
