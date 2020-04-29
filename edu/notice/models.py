from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce import HTMLField
# Create your models here.


class Notice(models.Model):
    slug = models.SlugField(max_length=255, unique=True, default='notice-slug')
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=200)
    notice_date = models.DateField()
    content = HTMLField('Content')
    informations = models.ManyToManyField('Information')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ecenter-notice-single', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = str(self.notice_date)+ "-" + slugify(self.title)
        return super(Notice, self).save(*args, **kwargs)

class Information(models.Model):
    information = models.CharField(max_length=200)

    def __str__(self):
        return self.information

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'

class HeaderNotice(models.Model):
    notice_heading_title = models.CharField(max_length=50)
    notice_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderNotice'