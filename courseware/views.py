from abc import ABC

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from courseware.forms import GroupEditForm, CourseEditForm, HtmlTEForm, ChapterEditForm, ReflectionForm
from courseware.models import Groups, Courses, TeachingElementBase, HtmlTE, Reflection, Chapters


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


class ListElements(ListView):
    model = TeachingElementBase
    fields = ['name']
    template_name = 'elements.html'

    def get_course_id(self):
        return self.kwargs['pk']


class AddHtmlElement(CreateView):
    form_class = HtmlTEForm
    model = HtmlTE
    context_object_name = 'element'
    template_name = 'html_element.html'

    def get_success_url(self):
        url = reverse('html_elements', kwargs={'pk': self.object.course_id})
        return url

    def get_form_kwargs(self):
        kwargs = super(AddHtmlElement, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs


class ListTEIElements(ListView, ABC):
    tei_type = None

    def get_course_id(self):
        return self.kwargs['pk']

    def get_queryset(self):
        return self.model.objects.filter(course=self.get_course_id())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_id'] = self.get_course_id()
        context['type'] = self.tei_type
        return context


class ListHtmlElements(ListTEIElements):
    model = HtmlTE
    context_object_name = 'elements'
    template_name = 'element_list.html'
    tei_type = "HTML"


class ListReflectionElements(ListTEIElements):
    model = Reflection
    context_object_name = 'elements'
    template_name = 'element_list.html'
    tei_type = "Reflection"


class AddReflectionElement(CreateView):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'

    def get_success_url(self):
        url = reverse('reflection_elements', kwargs={'pk': self.object.course_id})
        return url

    def get_form_kwargs(self):
        kwargs = super(AddReflectionElement, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs


class ListChapters(ListView):
    model = Chapters
    context_object_name = 'chapters'
    template_name = 'chapter_list.html'

    def get_course_id(self):
        return self.kwargs['pk']


class AddChapter(CreateView):
    model = Chapters
    fields = ['name']
    template_name = 'add_chapter.html'
    success_url = reverse_lazy('chapters')


class EditChapter(UpdateView):
    form_class = ChapterEditForm
    model = Chapters
    template_name = 'edit_chapter.html'
    success_url = reverse_lazy('chapters')


class EditHTMLElement(UpdateView):
    form_class = HtmlTEForm
    model = HtmlTE
    template_name = 'html_element.html'

    def get_success_url(self):
        url = reverse('html_elements', kwargs={'pk': self.object.course_id})
        return url

    def get_form_kwargs(self):
        kwargs = super(EditHTMLElement, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs


class EditReflectionElement(UpdateView):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'

    def get_success_url(self):
        url = reverse('reflection_elements', kwargs={'pk': self.object.course_id})
        return url

    def get_form_kwargs(self):
        kwargs = super(EditReflectionElement, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs
