import random

from django.db import models
from django.utils import timezone

from faker import Faker

from phonenumber_field.modelfields import PhoneNumberField

from core.validators import validate_email_for_prohibited_domain, validate_phone

from groups.models import Group


class Teacher(models.Model):

    faker = Faker()

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    birth_date = models.DateTimeField(null=False, default=timezone.now)
    age = models.IntegerField(null=False, default=42)
    email = models.EmailField(null=False, default=faker.email(), validators=[
        validate_email_for_prohibited_domain,
    ])
    phone_number = models.CharField(null=False, max_length=20, validators=[validate_phone])

    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='teachers'
    )

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {str(self.birth_date)[0:11]},\
                 {self.age}, {self.email}, {self.phone_number}, {self.group}'

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
