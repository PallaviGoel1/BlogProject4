from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from cloudinary.models import CloudinaryField
# Create your models here.

#STATUS = ((0, "Draft"),(1, "Submit"))
class Post(models.Model):
    title = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #status = models.IntegerField(choices=STATUS, default= 0)
    #featured_image = CloudinaryField('image', default='placeholder')
    #update_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    #created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")