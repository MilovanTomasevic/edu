from django.db import models
from tinymce import HTMLField


class Scholarship(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    content = HTMLField('Content')
    image = models.ImageField(default='scholarship/scholarship.png', upload_to='scholarship')

    def __str__(self):
        return self.title

    @property
    def areass(self):
        return self.areas_set.all()

class Areas(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='scholarship/scholarship-item-1.png', upload_to='scholarship')
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    requirements = models.ManyToManyField('Requirements')

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Requirements(models.Model):
    requirement = models.CharField(max_length=70)

    def __str__(self):
        return self.requirement

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'


class HeaderScholarship(models.Model):
    scholarship_heading_title = models.CharField(max_length=50)
    scholarship_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderScholarship'