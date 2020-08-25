from django.db import models
from centraldata.models import Student
from authentication.models import User
from company.models import Company
from topics.models import Topic
from lecturers.models import Lecturer

# Create your models here.

class Internship(models.Model):
    group = models.BooleanField(default=False)
    member = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    lecturer_adviser = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False, default='')
    end_date = models.DateField(blank=False, default='')
    title = models.CharField(max_length=255, blank=False, default='')
    intern_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    proposal = models.FileField(upload_to='uploads', blank=True)
    report = models.FileField(upload_to='uploads', blank=True)
    handout = models.FileField(upload_to='uploads', blank=True)
    ppt = models.FileField(upload_to='uploads', blank=True)
    publication_link = models.CharField(max_length=255, blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)