from django.forms import ModelForm, ModelMultipleChoiceField, CharField

from Elearn.settings import BASE_DIR
from loginUser.models import MyUser
from courseware.models import Groups, Courses, HtmlTE, Chapters, TeachingElementBase
from django.contrib.admin.widgets import FilteredSelectMultiple
from tinymce.widgets import TinyMCE
import os


class GroupEditForm(ModelForm):
    users = ModelMultipleChoiceField(queryset=MyUser.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='User',
                                            is_stacked=False),
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
                                            is_stacked=False),
                                     label='')

    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'teacher', 'groups']

    class Media:
        js = ['/admin/jsi18n/']
        css = {
            'all': (os.path.join(BASE_DIR, '/static/admin/css/widgets.css'),),
        }


class ChapterEditForm(ModelForm):
    elements = ModelMultipleChoiceField(queryset=TeachingElementBase.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='User',
                                            is_stacked=False),
                                     label='')

    class Meta:
        model = Chapters
        fields = ['name', 'elements']

    class Media:
        js = ['/admin/jsi18n/']
        css = {
            'all': (os.path.join(BASE_DIR, '/static/admin/css/widgets.css'),),
        }


class HtmlTEForm(ModelForm):
    html = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 50, 'class': 'form-control'}))

    class Meta:
        model = HtmlTE
        fields = ['name', 'description', 'html']
