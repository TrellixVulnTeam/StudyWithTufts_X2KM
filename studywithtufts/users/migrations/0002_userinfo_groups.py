# Generated by Django 2.2.6 on 2019-10-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_auto_20191012_0004'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, to='groups.StudyGroup'),
        ),
    ]
