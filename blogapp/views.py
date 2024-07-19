from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm , EditForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Code to display Likes on blogs
def LikeView(request, pk):
        post = get_object_or_404(Post,id=request.POST.get('post_id'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

# Code to display home page
class HomeView(ListView):
    model = Post
    cat= Category.objects.all()
    template_name = 'homepage.html'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# Code to display Categories list
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category.html',{'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
    Category_posts = Post.objects.filter(category=cats.replace('_',' '))
    return render(request,'categories.html', {'cats':cats.title().replace('_',' '), 'category_posts':Category_posts} )

# Code to display Blog detailed view
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()

        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        
        context["cat_menu"] = cat_menu
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes']= total_likes
        context["liked"] = liked
        return context

# Code to display Blog Create view
class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def blogView(request):
        current_user = request.user
        user_list = simpleList.objects.filter(author=current_user)
        return render(render, {'userlist': user_list})

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)
    
# Code to ddisplay category addition view
class AddCategoryView(CreateView):
   model = Category
   template_name = 'add_category.html'
   fields = '__all__'
   #ordering = ['category'] 

# Code to display comment addition view
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name ='add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy("home")
    
# Code to display edit bog view    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
   # ordering = ['-update_date']
    
# Code to display delete blog view
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("home")