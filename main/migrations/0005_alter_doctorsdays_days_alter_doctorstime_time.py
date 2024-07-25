# Generated by Django 4.2.4 on 2023-09-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_doctorsdays_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsdays',
            name='days',
            field=models.CharField(choices=[('Monday - Friday', 'Monday - Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=20, verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='doctorstime',
            name='time',
            field=models.CharField(choices=[('7:00 - 6:00', '7:00 - 6:00'), ('7:00 - 4:30', '7:00 - 4:30'), ('closed', 'closed')], max_length=20, verbose_name='Time'),
        ),
    ]
