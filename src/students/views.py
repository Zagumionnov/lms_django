from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from students.utils import format_list

from students.forms import StudentFilter


@csrf_exempt
def get_students(request):

    filter = StudentFilter(
        data=request.GET,
        queryset=Student.objects.all().order_by('-id')
    )

    return render(
        request=request,
        template_name='students-list.html',
        context={'filter': filter}
    )


@csrf_exempt
def create_student(request):
    if request.method == 'POST':

        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    else:

        form = StudentCreateForm()

    return render(
        request=request,
        template_name='students-create.html',
        context={'form': form}
    )


@csrf_exempt
def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentUpdateForm(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    else:

        form = StudentUpdateForm(instance=student)

    return render(
        request=request,
        template_name='students-update.html',
        context={'form': form}
    )
