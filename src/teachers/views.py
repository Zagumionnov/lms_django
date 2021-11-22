from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt

from students.utils import format_list

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all().order_by('-id')

    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'last_name',
        'age',
        'age__g',
        'email',
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            param_elems = param_value.split(',')
            if param_elems:
                or_filter = Q()
                for param_elem in param_elems:
                    or_filter |= Q(**{param_name: param_elem})
                teachers = teachers.filter(or_filter)
            else:
                teachers = teachers.filter(**{param_name: param_value})

    form = '''
    <form action="/teachers">
      <label >First name:</label><br>
      <input type="text" name="first_name" placeholder="First name"><br>
      <label >Last name:</label><br>
      <input type="text" name="last_name" placeholder="Last name"><br>
      <label >Age:</label><br>
      <input type="number" name="age" placeholder="Age"><br>
      <label >email:</label><br>
      <input type="email" name="email" placeholder="Email"><br><br>
      <input type="submit" value="Submit">
    </form>
    '''

    result = format_list(teachers)

    return HttpResponse(form + result)


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/teachers')

        return HttpResponseRedirect('/teachers')

    elif request.method == 'GET':

        form = TeacherCreateForm()

    html_template = '''
        <form method="post">
            {}

            <input type="submit" value="Create">
        </form>
        '''

    result = html_template.format(form.as_p())

    return HttpResponse(result)
