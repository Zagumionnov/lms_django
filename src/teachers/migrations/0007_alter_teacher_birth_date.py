# Generated by Django 3.2.9 on 2021-11-22 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_alter_teacher_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]