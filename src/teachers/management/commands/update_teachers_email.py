from django.core.management.base import BaseCommand, CommandError

from teachers.models import Teacher

from faker import Faker


class Command(BaseCommand):
    help = 'Updating teachers' # noqa

    def add_arguments(self, parser):
        parser.add_argument('start', type=int, help='starts id of updating teachers')
        parser.add_argument('stop', type=int, help='ends id of updating teachers')

    def handle(self, *args, **kwargs):

        faker = Faker()
        start = kwargs['start']
        stop = kwargs['stop']

        try:
            for i in range(start, stop + 1):
                teacher = Teacher.objects.get(id=i)
                teacher.email = faker.email()
                teacher.save()
        except CommandError as ce:
            raise CommandError(f'{ce}')

        self.stdout.write('Successfully')
