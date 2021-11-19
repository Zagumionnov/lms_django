from django.core.management.base import BaseCommand, CommandError

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates specified amount of teachers' # noqa

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The amount of added teachers')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        try:
            Teacher.generate_teachers(count)
        except CommandError as ce:
            raise CommandError(f'{ce}')
        self.stdout.write(f'Successfully generated {count} teachers')
