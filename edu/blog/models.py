from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class HeaderBlog(models.Model):
    blog_heading_title = models.CharField(max_length=50)
    blog_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderBlog'