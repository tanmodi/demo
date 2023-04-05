# Generated by Django 2.2.5 on 2019-10-08 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='back_pics/')),
                ('content', models.CharField(max_length=1000)),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]