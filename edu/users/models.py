from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(default='users/default.png', upload_to='users')
    fields = models.ForeignKey('Field' ,null=True ,on_delete=models.SET_NULL)
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
    description = models.TextField()
    phone = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    interests = models.ManyToManyField('Interests')
    biography = models.TextField()
    role = models.ManyToManyField('Role')

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

    def is_check_role(self, role):
        roles = self.user.userprofile.role.all()
        list_roles = []

        for r in roles:
            list_roles.append(r.name)
        if role in list_roles:
            return True
        return False

    def is_admin(self):
        roles = self.user.userprofile.role.all()
        admins= []

        for r in roles:
            admins.append(r.name)
        if 'admin' in admins:
            return True
        return False

    def is_teacher(self):
        roles = self.user.userprofile.role.all()
        teachers= []

        for r in roles:
            teachers.append(r.name)
        if 'teacher' in teachers:
            return True
        return False

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



