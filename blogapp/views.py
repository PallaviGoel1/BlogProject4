from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
#def home(request):
 #   return render(request, 'home.html',)

class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddBlogView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'



