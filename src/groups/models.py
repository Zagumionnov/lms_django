from django.db import models


class Group(models.Model):

    group_name = models.CharField(max_length=100, null=False)
    num_year = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.group_name}, {self.num_year}'
