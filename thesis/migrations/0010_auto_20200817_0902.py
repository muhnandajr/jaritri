# Generated by Django 3.0.8 on 2020-08-17 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200706_0318'),
        ('thesis', '0009_auto_20200814_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='company_name',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
        ),
    ]