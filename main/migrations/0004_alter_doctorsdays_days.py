# Generated by Django 4.2.4 on 2023-09-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_doctorsqualifications_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsdays',
            name='days',
            field=models.CharField(choices=[(0, 'Monday - Friday'), (1, 'Saturday'), (2, 'Sunday')], max_length=20, verbose_name='Day'),
        ),
    ]
