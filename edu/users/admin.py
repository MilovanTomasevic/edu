from django.contrib import admin

# Register your models here.
from .models import UserProfile , Category , Field, Interests



class PropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name' , 'fields' , 'category' , 'address']
    ist_display_links = ['user']
    search_fields = ['name' , 'fields', 'interests']
    list_filter = ['category' , 'fields', 'interests']
    filter_horizontal = ('interests',)

admin.site.register(UserProfile , PropertyAdmin)
admin.site.register(Category)
admin.site.register(Field)
admin.site.register(Interests)
