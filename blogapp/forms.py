from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','date','featured_image','author','body','likes')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','date','author','body','likes')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')