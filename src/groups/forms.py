from django.forms import ModelForm
import django_filters
from groups.models import Group


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = '__all__'


class GroupBaseForm(ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

    def as_div(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )


class GroupCreateForm(GroupBaseForm):
    pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        model = Group
        exclude = ['age']
