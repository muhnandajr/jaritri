# Generated by Django 3.0.8 on 2020-07-11 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centraldata', '0003_auto_20200711_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='avatar',
            new_name='student_avatar',
        ),
    ]
