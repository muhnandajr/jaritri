from django.db import models
from centraldata.models import Student
from company.models import Company
from topics.models import Topic
from lecturers.models import Lecturer

# Create your models here.

class Internship(models.Model):
    group = models.CharField(max_length=255, blank=False, default='')
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer_adviser = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    intern_year = models.IntegerField(blank=False, default='')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False, default='')
    end_date = models.DateField(blank=False, default='')
    intern_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    proposal = models.FileField(blank=True)
    report = models.FileField(blank=True)
    handout = models.FileField(blank=True)
    ppt_seminar = models.FileField(blank=True)
    publication_link = models.CharField(max_length=255, blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
