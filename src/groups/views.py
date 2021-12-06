from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from groups.forms import GroupCreateForm, GroupUpdateForm, GroupFilter
from groups.models import Group


def get_groups(request):
    filter = GroupFilter(
        data=request.GET,
        queryset=Group.objects.all().order_by('-id')
    )

    return render(
        request=request,
        template_name='groups-list.html',
        context={'filter': filter}
    )


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_group'))

    else:

        form = GroupCreateForm()

    return render(
        request=request,
        template_name='groups-create.html',
        context={'form': form}
    )


def update_group(request, id):
    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':

        form = GroupUpdateForm(
            data=request.POST,
            instance=group
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_group'))

    else:

        form = GroupUpdateForm(instance=group)

    return render(
        request=request,
        template_name='groups-update.html',
        context={
            'form': form,
            'group': group,
            'students': group.students.all(),
            'teachers': group.teachers.all()
                 }
        )


def delete_group(request, id):

    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list_group'))

    return render(
        request=request,
        template_name='groups-delete.html',
        context={'group': group}
    )
