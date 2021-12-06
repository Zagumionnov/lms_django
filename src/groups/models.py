from django.db import models

# from students.models import Student


class Group(models.Model):

    group_name = models.CharField(max_length=100, null=False)
    num_year = models.IntegerField(null=False, default=1)

    headman = models.OneToOneField(
        to='students.Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name='headed_group'
    )

    def __str__(self):
        return f'{self.group_name}'
