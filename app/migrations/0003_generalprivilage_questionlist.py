# Generated by Django 3.1.12 on 2021-09-21 07:48

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_generalprivilage_questionlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalprivilage',
            name='QuestionList',
            field=djongo.models.fields.JSONField(default=0),
            preserve_default=False,
        ),
    ]
