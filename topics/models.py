from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
