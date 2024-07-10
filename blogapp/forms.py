from django import forms
from .models import Post, Comment, Category
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','slug','author','category','content','snippet','blog_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
            #'author' : forms.TextInput(attrs={'class':'form-control','value':'', 'id': 'elder'}),
            'content' : SummernoteWidget(),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

        widgets = {
            #'title': forms.TextInput(attrs={'class':'form-control'}),
            'content' : SummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','content')