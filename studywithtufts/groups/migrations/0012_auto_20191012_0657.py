# Generated by Django 2.2.6 on 2019-10-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0011_auto_20191012_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='current_size',
            field=models.IntegerField(default=0),
        ),
    ]
