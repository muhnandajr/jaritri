from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    nim = models.CharField(max_length=255, blank=False, default='')
    number_phone = models.IntegerField(blank=False, default='')
    email = models.EmailField(blank=False, default='')
    village = models.CharField(max_length=50, blank=False, default='')
    rt_village = models.CharField(max_length=50, blank=False, default='')
    rw_village = models.CharField(max_length=50, blank=False, default='')
    sub_district = models.CharField(max_length=50, blank=False, default='')
    city = models.CharField(max_length=50, blank=False, default='')
    province = models.CharField(max_length=50, blank=False, default='')
    postal_code = models.IntegerField(blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
