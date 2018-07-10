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


class EditElement(UpdateView, ABC):

    def get_form_kwargs(self):
        kwargs = super(EditElement, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        url = None
        if self.object.type == "HTML":
            url = reverse('html_elements', kwargs={'pk': self.object.course_id})
        elif self.object.type == "Reflection":
            url = reverse('reflection_elements', kwargs={'pk': self.object.course_id})
        return url


class AddHtmlElement(EditElement):
    form_class = HtmlTEForm
    model = HtmlTE
    context_object_name = 'element'
    template_name = 'html_element.html'


class AddReflectionElement(EditElement):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'


class EditHTMLElement(EditElement):
    form_class = HtmlTEForm
    model = HtmlTE
    template_name = 'html_element.html'


class EditReflectionElement(EditElement):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'
