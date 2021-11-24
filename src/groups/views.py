from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm, GroupUpdateForm
from groups.models import Group

from groups.utils import format_list


def get_groups(request):
    groups = Group.objects.all().order_by('-id')

    params = [
        'group_name',
        'num_year'
    ]

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            param_elems = param_value.split(',')
            if param_elems:
                or_filter = Q()
                for param_elem in param_elems:
                    or_filter |= Q(**{param_name: param_elem})
                groups = groups.filter(or_filter)
            else:
                groups = groups.filter(**{param_name: param_value})

    form = '''
    <form action="/groups">
      <label >Group name:</label><br>
      <input type="text" name="group_name" placeholder="Group name"><br>
      <label >Level:</label><br>
      <input type="number" name="num_year" placeholder="Level"><br><br>
      <input type="submit" value="Submit">
    </form>
    '''

    result = format_list(groups)

    return HttpResponse(form + result)


@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

    elif request.method == 'GET':

        form = GroupCreateForm()

    html_template = '''
            <form method='post'>
                {}


                <input type="submit" value="Create">
            </form>
            '''

    result = html_template.format(form.as_p())

    return HttpResponse(result)


@csrf_exempt
def update_group(request, id):

    group = Group.objects.get(id=id)

    if request.method == 'POST':

        form = GroupUpdateForm(
            data=request.POST,
            instance=group
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

        return HttpResponseRedirect('/groups')

    elif request.method == 'GET':

        form = GroupUpdateForm(instance=group)

    html_template = '''
    <form method='post'>
        {}


        <input type="submit" value="Update">
    </form>
    '''

    result = html_template.format(form.as_p())

    return HttpResponse(result)

