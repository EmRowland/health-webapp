# Generated by Django 4.2.4 on 2023-09-29 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_appiontments_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiontments',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorsdepartment'),
        ),
        migrations.AlterField(
            model_name='appiontments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorsinit'),
        ),
    ]