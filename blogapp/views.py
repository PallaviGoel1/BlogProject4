from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-id']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ('title', 'body')
    



