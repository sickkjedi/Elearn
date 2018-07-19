from abc import ABC

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from courseware.forms import GroupEditForm, CourseEditForm, HtmlTEForm, ChapterEditForm, ReflectionForm, ChapterForm
from courseware.models import Groups, Courses, TeachingElementBase, HtmlTE, Reflection, Chapters


class ListGroups(ListView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'group_list.html'


class AddGroup(CreateView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'add_group.html'
    fields = ['group_name', 'description', 'year']

    def get_success_url(self):
        return reverse('groups')


class EditGroup(UpdateView):
    form_class = GroupEditForm
    model = Groups
    template_name = 'edit_group_course.html'

    def get_success_url(self):
        return reverse('groups')


class ListCourses(ListView):
    model = Courses
    context_object_name = 'courses'
    template_name = 'course_list.html'


class AddCourse(CreateView):
    model = Courses
    template_name = 'add_course.html'
    fields = ['course_name', 'description', 'teacher']

    def get_success_url(self):
        return reverse('courses')


class EditCourse(UpdateView):
    form_class = CourseEditForm
    model = Courses
    template_name = 'edit_group_course.html'

    def get_success_url(self):
        return reverse('courses')


class DeleteCourse(DeleteView):
    model = Courses

    def get_success_url(self):
        return reverse('courses')


class ListChapters(ListView):
    model = Chapters
    context_object_name = 'chapters'
    template_name = 'chapter_list.html'

    def get_course_id(self):
        return self.kwargs['pk']


class AddChapter(CreateView):
    form_class = ChapterForm
    model = Chapters
    template_name = 'add_chapter.html'

    def get_success_url(self):
        return reverse('chapters', kwargs={'pk': self.object.course_id})

    def get_form_kwargs(self):
        kwargs = super(AddChapter, self).get_form_kwargs()
        kwargs.update({'course_id': self.kwargs['pk']})
        return kwargs


class EditChapter(UpdateView):
    form_class = ChapterEditForm
    model = Chapters
    template_name = 'edit_chapter.html'

    def get_success_url(self):
        return reverse('chapters', kwargs={'pk': self.object.course_id})


class ListElements(ListView):
    model = TeachingElementBase
    context_object_name = 'elements'
    template_name = 'element_list.html'

    def get_chapter_id(self):
        return self.kwargs['pk']

    def get_queryset(self):
        return self.model.objects.filter(chapter=self.get_chapter_id())

    def get_context_data(self, **kwargs):
        context = super(ListElements, self).get_context_data(**kwargs)
        context['chapter_id'] = self.get_chapter_id()
        return context


class EditElement(UpdateView, CreateView, ABC):

    def get_form_kwargs(self):
        kwargs = super(EditElement, self).get_form_kwargs()
        kwargs.update({'chapter_id': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        url = None
        if self.object.type == "HTML":
            url = reverse('html_elements', kwargs={'pk': self.object.course_id})
        elif self.object.type == "Reflection":
            url = reverse('reflection_elements', kwargs={'pk': self.object.course_id})
        return url


class EditHTMLElement(EditElement):
    form_class = HtmlTEForm
    model = HtmlTE
    template_name = 'html_element.html'


class EditReflectionElement(EditElement):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'


class AddElement(CreateView, ABC):

    def get_form_kwargs(self):
        kwargs = super(AddElement, self).get_form_kwargs()
        kwargs.update({'chapter_id': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        return reverse('elements', kwargs={'pk': self.object.chapter_id})


class AddHtmlElement(EditElement):
    form_class = HtmlTEForm
    model = HtmlTE
    context_object_name = 'element'
    template_name = 'html_element.html'


class AddReflectionElement(AddElement):
    form_class = ReflectionForm
    model = Reflection
    template_name = 'reflection_element.html'

