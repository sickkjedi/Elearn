from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from courseware.models import Groups, Courses
from django.urls import reverse_lazy
from courseware.forms import GroupEditForm, CourseEditForm


class ListGroups(ListView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'group_list.html'


class AddGroup(CreateView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'add_group.html'
    success_url = reverse_lazy('groups')
    fields = ['group_name', 'description', 'year']


class EditGroup(UpdateView):
    form_class = GroupEditForm
    model = Groups
    template_name = 'edit_group_course.html'
    success_url = reverse_lazy('groups')


class ListCourses(ListView):
    model = Courses
    context_object_name = 'courses'
    template_name = 'course_list.html'


class AddCourse(CreateView):
    model = Courses
    context_object_name = 'courses'
    template_name = 'add_course.html'
    success_url = reverse_lazy('courses')
    fields = ['course_name', 'description', 'teacher']


class EditCourse(UpdateView):
    form_class = CourseEditForm
    model = Courses
    template_name = 'edit_group_course.html'
    success_url = reverse_lazy('courses')


