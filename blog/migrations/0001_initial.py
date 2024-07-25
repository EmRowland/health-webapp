# Generated by Django 4.2.4 on 2023-09-10 14:09

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs', verbose_name='blog image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=500, verbose_name='Blog Title')),
                ('blog_content', models.TextField(verbose_name='Blog content')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
            options={
                'verbose_name': 'Add Blog',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.CharField(max_length=200, unique=True, verbose_name='Category')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Add Blog Category',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, verbose_name='Tag')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Add Blog Tags',
            },
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150, verbose_name='commentors Name')),
                ('email', models.EmailField(max_length=254, verbose_name="Commentor's Email")),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ManyToManyField(to='blog.categories'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.tags'),
        ),
    ]
