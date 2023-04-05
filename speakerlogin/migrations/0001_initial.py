# Generated by Django 2.2.5 on 2019-10-12 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('username', models.CharField(blank=True, max_length=500)),
                ('email', models.CharField(max_length=250)),
                ('gender', models.CharField(blank=True, max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('mobileno', models.CharField(blank=True, max_length=250)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('zipcode', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='comments')),
                ('about', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]