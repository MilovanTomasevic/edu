from django.contrib import admin
from django import forms

from .models import UserProfile, Role
# Register your models here.
from .models import Course, HeaderCourses, Category, Requirements, Apply, FeesAndFunding, Lesson


class CourseForm(forms.ModelForm):
    try:
        teacher  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, help_text="Choose Teacher(s)", queryset=UserProfile.objects.filter(role__in=[Role.objects.get(pk=2)]))    
    except:
        teacher = None
class InLineLesson(admin.TabularInline):
    model = Lesson
    exclude = ('slug',)
    extra = 1
    max_num = 10

class CourseAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    form = CourseForm
    list_display = ['title', 'category', 'course_date', 'duration', 'price', 'slug']
    
    list_display_links = ['title']
    search_fields = ['title', 'category', 'course_date', 'duration', 'price']
    list_filter = ['duration', 'price', 'title' , 'category', 'course_date' ]
    filter_horizontal = ('requirements','apply', 'fees_and_funding', 'teacher')
    exclude = ('slug',)



class HeaderCourseAdmin(admin.ModelAdmin):
    list_display = ['courses_heading_title','courses_heading_message' ,]

admin.site.register(Course, CourseAdmin)
admin.site.register(HeaderCourses, HeaderCourseAdmin)

admin.site.register(Category)
admin.site.register(Requirements)
admin.site.register(Apply)
admin.site.register(FeesAndFunding)