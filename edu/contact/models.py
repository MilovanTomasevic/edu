from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    contact_heading_title = models.CharField(max_length=50)
    contact_heading_message = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    content = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)