from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(default='users/default.jpg', upload_to='users')
    fields = models.ForeignKey('Field' ,null=True ,on_delete=models.SET_NULL)
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    description = models.TextField()
    # mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    biography = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Field(models.Model):
    field_name = models.CharField(max_length=30)

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)