# Generated by Django 3.0.8 on 2020-08-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='graduate_year',
        ),
        migrations.AddField(
            model_name='thesis',
            name='nim',
            field=models.CharField(default='', max_length=50),
        ),
    ]