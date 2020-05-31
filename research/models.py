from django.db import models
from tinymce import HTMLField


class Research(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField('Content')
    image = models.ImageField(default='research/default.png', upload_to='research')

    def __str__(self):
        return self.title

class HeaderResearch(models.Model):
    research_heading_title = models.CharField(max_length=50)
    research_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderResearch'