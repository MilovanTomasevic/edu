from django.contrib import admin

# Register your models here.
from .models import UserProfile , Category , Field



class PropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name' , 'fields' , 'category' , 'address']
    ist_display_links = ['user']
    search_fields = ['name' , 'fields']
    list_filter = ['category' , 'fields']

admin.site.register(UserProfile , PropertyAdmin)
admin.site.register(Category)
admin.site.register(Field)
