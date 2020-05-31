from django.contrib import admin
from .models import Slider, Slide, Baner, Content, About, Training, Stories

class InLineSlide(admin.StackedInline):
    model = Slide
    extra = 1
    max_num = 5

class SliderAdmin(admin.ModelAdmin):
    inlines = [InLineSlide]

class InLineContent(admin.StackedInline):
    model = Content
    extra = 1
    max_num = 4

class BanerAdmin(admin.ModelAdmin):
    inlines = [InLineContent]


admin.site.register(Slider, SliderAdmin)
admin.site.register(Baner, BanerAdmin)
admin.site.register(About)
admin.site.register(Training)
admin.site.register(Stories)