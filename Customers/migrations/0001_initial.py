# Generated by Django 2.1.8 on 2020-07-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=70, verbose_name='Last Name')),
                ('address', models.CharField(max_length=70, verbose_name='Address')),
                ('mobile', models.CharField(max_length=70, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=70, verbose_name='Email Address')),
            ],
        ),
    ]