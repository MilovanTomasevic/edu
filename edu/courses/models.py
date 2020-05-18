from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from users.models import Role, UserProfile
from django.template.defaultfilters import slugify
from tinymce import HTMLField

# Create your models here.

class Course(models.Model):
    slug = models.SlugField(max_length=255, unique=True, default='course-slug')
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=200)
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    image = models.ImageField(default='courses/default.jpg', upload_to='courses')
    course_date = models.DateField()
    duration = models.PositiveIntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    price = models.FloatField(default=130)
    about_title = models.CharField(max_length=100)
    content = HTMLField('Content')
    requirements = models.ManyToManyField('Requirements')
    apply = models.ManyToManyField('Apply')
    fees_and_funding = models.ManyToManyField('FeesAndFunding')
    teacher = models.ManyToManyField('users.UserProfile')
    quantity = models.IntegerField(default=1)
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = str(self.course_date)+ "-" + slugify(self.title)
        return super(Course, self).save(*args, **kwargs)

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    slug = models.SlugField(max_length=255, unique=True, default='lesson-slug')
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField(default='courses/default.jpg', upload_to='courses')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail',
                        kwargs={'course_slug': self.course.slug,
                                'lesson_slug': self.slug
                       })
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)+ "-" + str(self.position)
        return super(Lesson, self).save(*args, **kwargs)

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
    fees_and_funding = HTMLField('Fees And Funding')

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
