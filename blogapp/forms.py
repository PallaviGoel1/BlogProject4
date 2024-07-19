from django import forms
from .models import Post, Comment, Category
from django_summernote.widgets import SummernoteWidget
from datetime import datetime

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

# Code to get information to add a blog
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','slug','category','content','snippet','blog_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content' : SummernoteWidget(attrs={'summernote':{'width': '100%'}}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }

# Code to get information to update a blog
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')
        model.update_date = datetime.now()

        widgets = {
            #'title': forms.TextInput(attrs={'class':'form-control'}),
            'content' : SummernoteWidget(attrs={'summernote':{'width': '100%'}}),
        }

# Code to get information to add a comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','content')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control'}),
        }