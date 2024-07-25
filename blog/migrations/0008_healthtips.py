# Generated by Django 4.2.4 on 2023-09-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comments_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150, verbose_name='Health Tips')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Add Daily Tips',
            },
        ),
    ]