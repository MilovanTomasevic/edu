from django.contrib import admin

from .models import About, Funfacts

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','stories_title']
    search_fields = ['title' , 'value']
    filter_horizontal = ('funfacts', 'peoples')

class FunfactsAdmin(admin.ModelAdmin):
    list_display = ['value', 'title']

admin.site.register(About, AboutAdmin)
admin.site.register(Funfacts, FunfactsAdmin)
