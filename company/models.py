from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    business = models.CharField(max_length=255, blank=False, default='')
    address = models.CharField(max_length=255, blank=False, default='')
    website = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=255, blank=True, default='')
    pic_name = models.CharField(max_length=255, blank=True, default='')
    pic_number = models.CharField(max_length=255, blank=True, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
