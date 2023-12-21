from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','date','author','body','status','likes')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','date','author','body','status','likes')
