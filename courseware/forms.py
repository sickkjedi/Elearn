from abc import ABC, abstractmethod

from django.forms import ModelForm, ModelMultipleChoiceField, CharField

from Elearn.settings import BASE_DIR
from loginUser.models import MyUser
from courseware.models import Groups, Courses, HtmlTE, Chapters, TeachingElementBase, Reflection
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

    chapters = ModelMultipleChoiceField(queryset=Chapters.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='Chapters',
                                            is_stacked=False),
                                     label='')

    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'teacher', 'groups', 'chapters']

    class Media:
        js = ['/admin/jsi18n/']
        css = {
            'all': (os.path.join(BASE_DIR, '/static/admin/css/widgets.css'),),
        }


class ChapterEditForm(ModelForm):
    elements = ModelMultipleChoiceField(queryset=TeachingElementBase.objects.all(),
                                        required=False,
                                        widget=FilteredSelectMultiple(
                                            verbose_name='Elements',
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

    def __init__(self, *args, **kwargs):
        self.course_id = kwargs.pop('course_id', None)
        super(HtmlTEForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(HtmlTEForm, self).save(commit=False)
        if not instance.course_id:
            instance.course_id = self.course_id
        if commit:
            instance.save()
        return instance


class ReflectionForm(ModelForm):

    class Meta:
        model = Reflection
        fields = ['name', 'description', 'question']

    def __init__(self, *args, **kwargs):
        self.course_id = kwargs.pop('course_id', None)
        super(ReflectionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ReflectionForm, self).save(commit=False)
        if not instance.course_id:
            instance.course_id = self.course_id
        if commit:
            instance.save()
        return instance

