# Generated by Django 4.2.4 on 2023-09-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_healthtips_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthtips',
            name='content',
            field=models.TextField(verbose_name='Health Tips'),
        ),
    ]