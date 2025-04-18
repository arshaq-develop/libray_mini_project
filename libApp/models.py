from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    bookname = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    options = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )
    status = models.CharField(max_length=100, choices=options, default='Available')
