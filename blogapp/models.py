from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.

#STATUS = ((0, "Draft"),(1, "Submit"))
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug =models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    likes = models.ManyToManyField(User, blank=True)
    #status = models.IntegerField(choices=STATUS, default=True)
    featured_image = CloudinaryField('image', default='placeholder')
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

