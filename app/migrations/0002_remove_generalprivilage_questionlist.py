# Generated by Django 3.1.12 on 2021-09-21 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalprivilage',
            name='QuestionList',
        ),
    ]