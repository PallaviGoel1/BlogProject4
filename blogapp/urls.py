from django.urls import path
from .views import HomeView, BlogDetailView, AddBlogView

urlpatterns = [
    path('',HomeView.as_view(), name ="home"),
    path('Blog/<int:pk>',BlogDetailView.as_view(), name = "post_detail"),
    path('add_post/',AddBlogView.as_view(), name = "add_post"),
]