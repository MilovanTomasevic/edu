from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce import HTMLField
# Create your models here.


class Event(models.Model):
    slug = models.SlugField(max_length=255, unique=True, default='event-slug')
    title = models.CharField(max_length=100)
    image = models.ImageField(default='events/default.jpg', upload_to='events')
    short_content = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    price = models.DecimalField(default=99.99, max_digits=6, decimal_places=2)
    content = HTMLField('Content')
    speakers = models.ManyToManyField('users.UserProfile')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ecenter-events-single', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        # self.slug = str(self.event_date)+ "-" + slugify(self.title)
        self.slug = slugify(self.title)
        return super(Event, self).save(*args, **kwargs)


class HeaderEvents(models.Model):
    events_heading_title = models.CharField(max_length=50)
    events_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderEvents'