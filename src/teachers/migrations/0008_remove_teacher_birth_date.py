# Generated by Django 3.2.9 on 2021-11-22 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_alter_teacher_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='birth_date',
        ),
    ]
