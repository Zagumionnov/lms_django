
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


@csrf_exempt
def get_teachers(request):

    filter = TeacherFilter(
        data=request.GET,
        queryset=Teacher.objects.all().order_by('-id')
    )

    return render(
        request=request,
        template_name='teachers-list.html',
        context={'filter': filter}
    )


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('list_teacher'))

    else:

        form = TeacherCreateForm()

    return render(
        request=request,
        template_name='teachers-create.html',
        context={'form': form}
    )

@csrf_exempt
def update_teacher(request, id):

    teacher = Teacher.objects.get(id=id)

    if request.method == 'POST':

        form = TeacherUpdateForm(
            data=request.POST,
            instance=teacher
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_teacher'))

    else:

        form = TeacherUpdateForm(instance=teacher)

    return render(
        request=request,
        template_name='students-update.html',
        context={'form': form}
    )