# Generated by Django 3.2.9 on 2021-11-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='academic_title',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='experience',
        ),
    ]