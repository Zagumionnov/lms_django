# Generated by Django 3.2.9 on 2021-11-22 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_teacher_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 15, 10, 27, 807136, tzinfo=utc)),
        ),
    ]
