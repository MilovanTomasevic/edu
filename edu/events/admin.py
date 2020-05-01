from django.contrib import admin
from .models import Event, HeaderEvents

class EventAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    ordering = ('-event_date',)
    filter_horizontal = ('speakers',)
    list_display = ['title' , 'event_date']
    list_display_links = ['title']
    search_fields = ['title' , 'event_date']
    list_filter = ['title' , 'event_date']


admin.site.register(Event, EventAdmin)
admin.site.register(HeaderEvents)