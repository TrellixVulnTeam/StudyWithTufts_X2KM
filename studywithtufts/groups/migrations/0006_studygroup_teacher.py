# Generated by Django 2.2.6 on 2019-10-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20191011_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='teacher',
            field=models.CharField(default='', max_length=100),
        ),
    ]
