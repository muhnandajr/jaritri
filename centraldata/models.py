from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=255, blank=False, default='')
    student_nim = models.CharField(max_length=255, blank=False, default='')
    student_number_phone = models.IntegerField(blank=False, default='')
    student_email = models.CharField(max_length=255, blank=False, default='')
    file = models.ImageField(upload_to='images/', blank=False, default='')
    student_address = models.CharField(max_length=255, blank=False, default='')
    student_city = models.CharField(max_length=255, blank=False, default='')
    student_province = models.CharField(max_length=255, blank=False, default='')
    student_postal_code = models.IntegerField(blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
