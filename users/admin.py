from django.contrib import admin

# Register your models here.
from .models import UserProfile , Category , Field, Interests, Role



class UsersAdmin(admin.ModelAdmin):
    list_display = ['user', 'name' , 'fields' , 'category' , 'address']
    list_display_links = ['user']
    search_fields = ['role', 'name' , 'fields', 'interests']
    list_filter = ['role', 'category' , 'fields', 'interests']
    filter_horizontal = ('interests','role',)


admin.site.register(UserProfile , UsersAdmin)
admin.site.register(Category)
admin.site.register(Field)
admin.site.register(Interests)
admin.site.register(Role)
