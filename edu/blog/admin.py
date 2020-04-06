from django.contrib import admin

# Register your models here.
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ['author','title' , 'date_posted']
    list_display_links = ['title']
    search_fields = ['title' , 'date_posted']
    list_filter = ['title' , 'date_posted']

admin.site.register(Post, BlogAdmin)