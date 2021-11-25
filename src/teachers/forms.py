from django.core.exceptions import ValidationError
from django.forms import ModelForm

import django_filters
from teachers.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherBaseForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

    def as_div(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    def clean_email(self):

        email = self.cleaned_data['email']

        exists_students = Teacher.objects.filter(email=email).exclude(id=self.instance.id).exists()

        if exists_students:
            raise ValidationError('Email is not unique!')

        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        model = Teacher
        exclude = ['age']
