from django.core.exceptions import ValidationError
from django.forms import ModelForm

from teachers.models import Teacher


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

    def clean_phone_number(self):
        SHORT_LENGTH = 13  # noqa

        phone_number = self.cleaned_data['phone_number']

        if len(phone_number) == SHORT_LENGTH:
            phone_number = '+38' + phone_number

        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']

        existing_emails = []
        for e in Teacher.objects.values('email'):
            existing_emails.append(e["email"])
        if self.initial:
            existing_emails.remove(self.initial["email"])

        if email in existing_emails:
            raise ValidationError(f'{email} - teacher with this email already exists.')

        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        model = Teacher
        exclude = ['age']
