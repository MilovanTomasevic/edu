from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=100)
    content = HTMLField('Content')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', default='posts/default.png')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
    
    @property
    def get_comments(self):
        return self.comments.all().filter(parent=None)

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-timestamp',)
    
    def __str__(self):
        return 'Comment by {} for {}'.format(self.user.username, self.post.title)

    def get_replies(self):
        return Comment.objects.filter(parent=self)
    

class HeaderBlog(models.Model):
    blog_heading_title = models.CharField(max_length=50)
    blog_heading_message = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'
        db_table = 'HeaderBlog'