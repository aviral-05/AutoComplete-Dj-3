# Generated by Django 2.1.8 on 2020-07-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_auto_20200721_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('0', 'Male'), ('1', 'Female')], max_length=30, null=True, verbose_name='Gender'),
        ),
    ]
