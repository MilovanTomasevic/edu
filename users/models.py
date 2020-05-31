from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
from tinymce import HTMLField

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(default='users/default.png', upload_to='users')
    fields = models.ForeignKey('Field' ,null=True ,on_delete=models.SET_NULL)
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    description = HTMLField('Description')
    phone = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    interests = models.ManyToManyField('Interests')
    biography = HTMLField('Biography')
    role = models.ManyToManyField('Role') # models.ForeignKey('Role', related_name='roles')
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def is_teacher(self):
        return [r.name for r in self.user.userprofile.role.all() if r.name in "teacher"]

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Field(models.Model):
    field_name = models.CharField(max_length=50)

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'

class Interests(models.Model):
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest

    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
