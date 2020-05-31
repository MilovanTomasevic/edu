from django.db import models
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(default='home/banner-1.jpg', upload_to='home')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    @property
    def slides(self):
        return self.slide_set.all().order_by('position')

class Slide(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    position = models.IntegerField()
    slider = models.ForeignKey(Slider, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
class Baner(models.Model):
    image = models.ImageField(default='home/banner-2.png', upload_to='home')

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'Baner'
        verbose_name_plural = 'Baners'

    @property
    def contents(self):
        return self.content_set.all()

class Content(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('Content')
    themify_icons = models.CharField(max_length=15, default='ti-face-smile')
    baner = models.ForeignKey(Baner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('Content')
    image = models.ImageField(default='home/about-us.jpg', upload_to='home')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class Training(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

class Stories(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('Content')
    image = models.ImageField(default='home/success-story.jpg', upload_to='home')
    video = models.CharField(max_length=200)

    def __str__(self):
        return self.title