import datetime
import random

from django.db import models

from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)

    email = models.EmailField(max_length=64)
    phone_number = models.CharField(null=False, max_length=20)

    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return f'{self.first_name},' \
               f'{self.last_name},' \
               f'{self.email},' \
               f'{self.phone_number},' \
               f'{self.age}'

    @classmethod
    def generate_students(cls, count):
        faker = Faker()

        for _ in range(count):
            new_object = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(10, 105)
            )

            new_object.save()
