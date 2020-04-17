from django.contrib import admin

# Register your models here.
from .models import Course, HeaderCourses, Category, Requirements, Apply, FeesAndFunding

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'course_date', 'duration', 'price']
    list_display_links = ['title']
    search_fields = ['title', 'category', 'course_date', 'duration', 'price']
    list_filter = ['duration', 'price', 'title' , 'category', 'course_date' ]
    filter_horizontal = ('requirements','apply', 'fees_and_funding', 'teacher')

class HeaderCourseAdmin(admin.ModelAdmin):
    list_display = ['courses_heading_title','courses_heading_message' ,]

admin.site.register(Course, CourseAdmin)
admin.site.register(HeaderCourses, HeaderCourseAdmin)

admin.site.register(Category)
admin.site.register(Requirements)
admin.site.register(Apply)
admin.site.register(FeesAndFunding)