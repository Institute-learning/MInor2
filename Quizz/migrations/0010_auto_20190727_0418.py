# Generated by Django 2.2.3 on 2019-07-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0009_quiz_quizname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='id',
        ),
        migrations.AlterField(
            model_name='batch',
            name='batchName',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]