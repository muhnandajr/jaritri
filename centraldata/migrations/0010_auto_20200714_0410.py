# Generated by Django 3.0.8 on 2020-07-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centraldata', '0009_auto_20200714_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
