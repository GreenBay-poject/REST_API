# Generated by Django 3.1.12 on 2021-08-17 15:27

import app.Models.Answeres
import app.Models.Note
import app.Models.Posts
import app.Models.Token
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthPrivilage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_refrence', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=200)),
                ('FeedPosts', djongo.models.fields.ArrayField(model_container=app.Models.Posts.Posts, model_form_class=app.Models.Posts.PostsForm)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Question', models.CharField(max_length=200)),
                ('DatePosted', models.DateTimeField()),
                ('AnsweresList', djongo.models.fields.ArrayField(model_container=app.Models.Answeres.Answeres, model_form_class=app.Models.Answeres.AnsweresForm)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('UserEmail', models.EmailField(max_length=50)),
                ('UserPassword', models.CharField(max_length=50)),
                ('UserAge', models.IntegerField()),
                ('IsAuhtorized', models.BooleanField()),
                ('Gender', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=500)),
                ('PostalCode', models.IntegerField()),
                ('DateRegistered', models.DateTimeField()),
                ('Notes', djongo.models.fields.ArrayField(model_container=app.Models.Note.Note, model_form_class=app.Models.Note.NoteForm)),
                ('Tokens', djongo.models.fields.ArrayField(model_container=app.Models.Token.Token, model_form_class=app.Models.Token.TokenForm)),
                ('Privilage', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralPrivilage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionList', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='app.questions')),
            ],
        ),
    ]
