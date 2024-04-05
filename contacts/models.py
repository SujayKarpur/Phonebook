from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class Usero(AbstractUser):
    #name = models.CharField(max_length=100)
    number = PhoneNumberField(unique=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = PhoneNumberField(unique=True)

    class relationship(models.TextChoices):
        family = 'family'
        friend = 'friend'
        colleague = 'colleague'
        partner = 'partner'
        other = 'other'

    relationship_type = models.TextField(choices = relationship.choices, default = relationship.other)


    email = models.EmailField(default = '', blank = True, null = True)

    info = models.TextField(default='',blank=True,null=True)
    
    
    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Usero, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs = {'pk' : self.pk})