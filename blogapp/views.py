from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm , EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.

def LikeView(request, pk):
        post = get_object_or_404(Post,id=request.POST.get('post_id'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-date']
    paginate_by = 6

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    
class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ('title', 'body')
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = [ 'title', 'slug', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("home")