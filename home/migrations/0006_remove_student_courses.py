# Generated by Django 3.0.5 on 2020-05-11 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_stud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]