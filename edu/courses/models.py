from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.signals import post_save
from users.models import Role, UserProfile

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=200)
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    image = models.ImageField(default='courses/default.jpg', upload_to='users')
    course_date = models.DateField()
    duration = models.PositiveIntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    price = models.DecimalField(default=99.99, max_digits=6, decimal_places=2)
    about_title = models.CharField(max_length=100)
    content = models.TextField()
    requirements = models.ManyToManyField('Requirements')
    apply = models.ManyToManyField('Apply')
    fees_and_funding = models.ManyToManyField('FeesAndFunding')
    teacher = models.ManyToManyField('users.UserProfile')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Requirements(models.Model):
    requirement = models.CharField(max_length=200)

    def __str__(self):
        return self.requirement

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'


class Apply(models.Model):
    apply = models.CharField(max_length=200)

    def __str__(self):
        return self.apply

    class Meta:
        verbose_name = 'Apply'
        verbose_name_plural = 'Apply'

class FeesAndFunding(models.Model):
    fees_and_funding = models.TextField()

    def __str__(self):
        return self.fees_and_funding

    class Meta:
        verbose_name = 'Fees And Funding'
        verbose_name_plural = 'Fees And Funding'


class HeaderCourses(models.Model):
    courses_heading_title = models.CharField(max_length=50)
    courses_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderCourses'

def course_created(instance, **kwargs):
    if kwargs["created"]:
        # instance.role.add(Role.objects.get(pk=2))
        print("Kurs kreiran ! ")


post_save.connect(course_created, sender=Course)