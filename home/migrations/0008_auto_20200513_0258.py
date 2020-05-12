# Generated by Django 3.0.5 on 2020-05-12 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200513_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correctoption',
            field=models.CharField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], default=models.CharField(default=' ', max_length=50), max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='quizName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.quiz'),
        ),
    ]