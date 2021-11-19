from django.http import HttpResponse

from students.models import Student
from students.utils import format_list


def get_students(request):

    students = Student.objects.all()

    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'last_name',
        'age',
        'age__g'
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            students = students.filter(**{param_name: param_value})

    result = format_list(students)

    return HttpResponse(result)
