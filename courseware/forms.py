from django.forms import ModelForm, ModelMultipleChoiceField

from Elearn.settings import BASE_DIR
from loginUser.models import MyUser
from courseware.models import Groups, Courses
from django.contrib.admin.widgets import FilteredSelectMultiple
import os


class GroupEditForm(ModelForm):
    users = ModelMultipleChoiceField(queryset=MyUser.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='User',
                                            is_stacked=False ),
                                     label='')
    class Meta:
        model = Groups
        fields = ['group_name', 'description', 'year', 'users']

    class Media:
        js = ['/admin/jsi18n/']
        css = {
            'all': (os.path.join(BASE_DIR, '/static/admin/css/widgets.css'),),
        }


class CourseEditForm(ModelForm):
    groups = ModelMultipleChoiceField(queryset=Groups.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='Groups',
                                            is_stacked=False ),
                                     label='')
    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'teacher', 'groups']

    class Media:
        js = ['/admin/jsi18n/']
        css = {
            'all': (os.path.join(BASE_DIR, '/static/admin/css/widgets.css'),),
        }
