# Generated by Django 4.2.4 on 2023-09-22 21:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_slug_remove_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='fff', editable=False, populate_from='title'),
        ),
    ]