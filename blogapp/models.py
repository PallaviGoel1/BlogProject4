from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null= True, on_delete= models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/" )
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return  str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255, unique= False)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,related_name = 'blogpost_like', blank= True)
    update_date = models.DateTimeField(default=timezone.now)
    snippet = models.CharField(max_length=255)
    blog_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    
    
    class Meta:
        ordering = ['-date_posted']

    def update(self, *args, **kwargs):
        kwargs.update({'update_date': timezone.now})
        super().update(*args, **kwargs)

        return self

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    content = models.TextField()
    date_posted =  models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    #class Meta:
     #   ordering = ["date_posted"]
   
    def __str__(self):
        return '%s-%s' % (self.post.title, self.name)
       