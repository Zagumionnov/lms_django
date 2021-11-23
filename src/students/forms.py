from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student


class StudentBaseForm(ModelForm):

    class Meta:
        model = Student
        # fields = ['first_name', 'last_name', 'age']
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
