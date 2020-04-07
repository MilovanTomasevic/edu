from django.db import models

class About(models.Model):
    about_heading_title = models.CharField(max_length=50)
    about_heading_message = models.CharField(max_length=150)
    image = models.ImageField(upload_to='about/')
    title =models.CharField(max_length=150)
    content = models.TextField()
    funfacts = models.ManyToManyField('Funfacts')
    stories_title = models.CharField(max_length=50)
    stories_content = models.TextField()
    story_backgroung = models.ImageField(upload_to='about/', null=True)
    video = models.CharField(max_length=50)
    title_people = models.CharField(max_length=50)
    peoples = models.ManyToManyField('users.UserProfile')

    def __str__(self):
        return str(self.id)

class Funfacts(models.Model):
    value = models.IntegerField()
    title = models.CharField(max_length=20)

    def __str__(self):
            return self.title