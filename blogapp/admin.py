from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


#@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'date')
    search_fields = ['title', 'body']
    list_filter = ( 'slug','date')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
admin.site.register(Post, PostAdmin)



