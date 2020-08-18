# Generated by Django 3.0.8 on 2020-08-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200806_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='zip',
            new_name='postal_code',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rt_village',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rw_village',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sub_district',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='village',
            field=models.CharField(default='', max_length=50),
        ),
    ]
