from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(Comment)
admin.site.register(Category)


#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'date')
    search_fields = ['title', 'body']
    list_filter = ( 'slug','date')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    list_per_page = 4
admin.site.register(Post, PostAdmin)



