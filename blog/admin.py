from django.contrib import admin

# Register your models here.
from .models import Post, HeaderBlog, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ['author','title' , 'date_posted']
    list_display_links = ['title']
    search_fields = ['title' , 'date_posted']
    list_filter = ['title' , 'date_posted']

    filter_horizontal = ('categories',)

class HeaderAdmin(admin.ModelAdmin):
    list_display = ['blog_heading_title','blog_heading_message' ,]

admin.site.register(Post, BlogAdmin)
admin.site.register(HeaderBlog, HeaderAdmin)
admin.site.register(Category)
admin.site.register(Comment)