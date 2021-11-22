import random

from django.db import models
from django.utils import timezone

from faker import Faker

from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    birth_date = models.DateTimeField(null=False, default=timezone.now)
    age = models.IntegerField(null=False, default=42)
    email = models.EmailField(null=False, default='email@email.com')
    phone_number = PhoneNumberField(null=False, default='+41524204242')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.birth_date}, {self.age}, {self.email}, {self.phone_number}'

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
