from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

#admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)
#@admin.register(Post, PostAdmin)

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'date_posted')
    search_fields = ['title', 'content']
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
