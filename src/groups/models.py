from django.db import models


class Group(models.Model):

    group_name = models.CharField(max_length=100, null=False)
    num_year = models.IntegerField(null=False, default=1)
    number_of_students = models.IntegerField(null=False)
