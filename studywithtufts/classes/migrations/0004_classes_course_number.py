# Generated by Django 2.2.6 on 2019-10-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_remove_classes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='course_number',
            field=models.IntegerField(default=0),
        ),
    ]
