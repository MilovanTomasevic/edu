from django.contrib import admin
from .models import Scholarship, Areas, HeaderScholarship, Category, Requirements

class InLineAreas(admin.TabularInline):
    model = Areas
    filter_horizontal = ('requirements',)
    extra = 1
    max_num = 10

class ScholarshipAdmin(admin.ModelAdmin):
    inlines = [InLineAreas]


admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(HeaderScholarship)
admin.site.register(Category)
admin.site.register(Requirements)