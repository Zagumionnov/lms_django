
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):

    filter = TeacherFilter(
        data=request.GET,
        queryset=Teacher.objects.all().select_related('group').order_by('-id')
    )

    return render(
        request=request,
        template_name='teachers-list.html',
        context={'filter': filter}
    )


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


def update_teacher(request, id):

    teacher = get_object_or_404(Teacher, id=id)

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
        template_name='teachers-update.html',
        context={'form': form}
    )


def delete_teacher(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('list_teacher'))

    return render(
        request=request,
        template_name='teachers-delete.html',
        context={'teacher': teacher}
    )
