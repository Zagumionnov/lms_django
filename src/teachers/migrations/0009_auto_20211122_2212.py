# Generated by Django 3.2.9 on 2021-11-22 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_remove_teacher_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 22, 12, 4, 265803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='thomas38@example.com', max_length=254),
        ),
    ]
