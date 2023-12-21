from django.urls import path
from .views import HomeView, BlogDetailView, AddBlogView, LikeView, UpdatePostView, DeletePostView

urlpatterns = [
    path('',HomeView.as_view(), name ="home"),
    path('Blog/<int:pk>',BlogDetailView.as_view(), name = "post_detail"),
    path('add_post/',AddBlogView.as_view(), name = "add_post"),
    path('Blog/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
    path('likes/<int:pk>', LikeView, name= 'like_post'),
    path('Blog/edit/<int:pk>/delete',DeletePostView.as_view(), name= 'delete_post'),
]