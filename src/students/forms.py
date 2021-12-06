import re

import django_filters
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }


class StudentBaseForm(ModelForm):

    class Meta:
        model = Student
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

        existing_emails = []
        for e in Student.objects.values('email'):
            existing_emails.append(e["email"])
        if self.initial:
            existing_emails.remove(self.initial["email"])

        if email in existing_emails:
            raise ValidationError(f'{email} - student with this email already exists.')

        return email

    def clean(self):
        result = super().clean()

        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']

        if enroll_date > graduate_date:
            raise ValidationError('Enroll date couldn\'t be after graduate date')

        return result


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        model = Student
        exclude = ['age']
