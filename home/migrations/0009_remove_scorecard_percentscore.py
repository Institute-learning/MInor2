# Generated by Django 3.0.5 on 2020-05-15 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_scorecard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorecard',
            name='percentScore',
        ),
    ]