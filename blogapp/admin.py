from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Category)
admin.site.register(Profile)


class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'date_posted')
    search_fields = ['title', 'content']
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

