from django.contrib import admin
from .models import Notice, Information, HeaderNotice

class NoticeAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    ordering = ('-notice_date',)
    filter_horizontal = ('informations',)
    list_display = ['title' , 'notice_date']
    list_display_links = ['title']
    search_fields = ['title' , 'notice_date']
    list_filter = ['title' , 'notice_date']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Information)
admin.site.register(HeaderNotice)