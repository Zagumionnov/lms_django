import random

from django.db import models
from faker import Faker


class Teacher(models.Model):

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    age = models.IntegerField(null=False, default=42)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}'

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()

        for _ in range(count):
            new_object = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(25, 105)
            )

            new_object.save()
