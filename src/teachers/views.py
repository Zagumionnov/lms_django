from django.http import HttpResponse
from django.shortcuts import render  # noqa
from students.utils import format_list
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()

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
            teachers = teachers.filter(**{param_name: param_value})

    result = format_list(teachers)

    return HttpResponse(result)
