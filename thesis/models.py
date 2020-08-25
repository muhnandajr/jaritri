from django.db import models
from centraldata.models import Student
from authentication.models import User
from company.models import Company
from topics.models import Topic
from lecturers.models import Lecturer
from rest_framework_tricks.models.fields import NestedProxyField

# Create your models here.

class Thesis(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    thesis_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    thesis_title = models.CharField(max_length=255, blank=False, default='')
    lecturer_adviser = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    thesis_proposal = models.FileField(upload_to='uploads', blank=True)
    thesis_report = models.FileField(upload_to='uploads',blank=True)
    thesis_handout = models.FileField(upload_to='uploads',blank=True)
    thesis_ppt = models.FileField(upload_to='uploads',blank=True)
    publication_link = models.CharField(max_length=255, blank=False, default='')
    internship_status = models.BooleanField(default=False)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, default='1')
    start_date = models.DateField(blank=True, default='2000-01-01')
    end_date = models.DateField(blank=True, default='2000-01-01')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    internship = NestedProxyField(
        'company_name',
        'start_date',
        'end_date',
    )
