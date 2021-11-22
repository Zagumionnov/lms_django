from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm
from students.models import Student
from students.utils import format_list


def get_students(request):
    students = Student.objects.all().order_by('-id')

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
            param_elems = param_value.split(',')
            if param_elems:
                or_filter = Q()
                for param_elem in param_elems:
                    or_filter |= Q(**{param_name: param_elem})
                students = students.filter(or_filter)
            else:
                students = students.filter(**{param_name: param_value})

    form = '''
    <form action="/students">

      <label >First name:</label><br>
      <input type="text" name="first_name" placeholder="Enter first name"><br>

      <label >Last name:</label><br>
      <input type="text" name="last_name" placeholder="Enter last name"><br>

      <label >Age:</label><br>
      <input type="number" name="age" placeholder=Enter age><br><br>

      <input type="submit" value="Submit">
    </form> '''

    result = format_list(students)

    return HttpResponse(form + result)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':

        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

        return HttpResponseRedirect('/students')

    elif request.method == 'GET':

        form = StudentCreateForm()

    html_template = '''
    <form method='post'>
        {}


        <input type="submit" value="Create">
    </form>
    '''

    result = html_template.format(form.as_p())

    return HttpResponse(result)
