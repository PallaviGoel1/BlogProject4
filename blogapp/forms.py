from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','date','featured_image','author','body')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','date','author','body')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')