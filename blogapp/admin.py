from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

#admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)
#@admin.register(Post, PostAdmin)

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'date')
    search_fields = ['title', 'body']
    list_filter = ('status','title')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
   
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'approved')
    list_filter = ('approved','name')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

