# Generated by Django 3.0.8 on 2020-08-11 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thesis', '0003_auto_20200811_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]