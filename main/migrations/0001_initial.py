# Generated by Django 4.2.4 on 2023-09-02 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsDAys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[(0, 'Monday - Friday'), (1, 'Saturday'), (2, 'Sunday')], max_length=20, verbose_name='Work Days')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsInit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='Doctors Name')),
                ('work', models.CharField(max_length=1000, verbose_name='Area of Speciality')),
                ('about', models.TextField(verbose_name='About The Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[(0, '7:00 - 6:00'), (1, '7:00 - 4:30'), (2, 'closed')], max_length=20, verbose_name='Work time')),
                ('days', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.doctorsdays')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsWorkHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorsinit')),
                ('work_time', models.ManyToManyField(to='main.doctorstime')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsQualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, verbose_name='Schooling Period')),
                ('qualification_school', models.CharField(max_length=300, verbose_name='Add qualification and School')),
                ('description', models.TextField(verbose_name='write Description')),
                ('skills', models.TextField(verbose_name='write About Skills')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorsinit')),
            ],
            options={
                'verbose_name': 'Add Doctors Qualifications',
            },
        ),
    ]