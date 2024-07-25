# Generated by Django 4.2.4 on 2023-09-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_subscription_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appiontments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=200, verbose_name='Doctor')),
                ('department', models.CharField(max_length=200, verbose_name='Department')),
                ('time', models.DateTimeField(verbose_name='Appiontment Time')),
                ('fullname', models.CharField(max_length=150, verbose_name='Full Name')),
                ('phone', models.IntegerField(verbose_name='Phone Number')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Appointments',
            },
        ),
    ]