from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from courseware.models import Groups, Courses, TeachingElementBase, HtmlTE, Reflection, Chapters
from django.urls import reverse_lazy
from courseware.forms import GroupEditForm, CourseEditForm, HtmlTEForm, ChapterEditForm


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


class ListHtmlElements(ListView):
    model = HtmlTE
    context_object_name = 'elements'
    template_name = 'element_list.html'

    def get_course_id(self):
        return self.kwargs['pk']


class AddHtmlElement(CreateView):
    from_class = HtmlTEForm
    model = HtmlTE
    context_object_name = 'element'
    template_name = 'html_element.html'
    fields = ['name', 'description', 'html']
    success_url = reverse_lazy('html_elements')

    # def get_form_kwargs(self):
    #     kwargs = super(AddHtmlElement, self).get_form_kwargs()
    #     kwargs.update({'course_id': self.kwargs['pk']})
    #     return kwargs

    # def get_course_id(self):
    #     return self.kwargs['pk']


class ListReflectionElements(ListView):
    model = Reflection
    context_object_name = 'elements'
    template_name = 'element_list.html'


class AddReflectionElement(CreateView):
    model = Reflection
    template_name = 'reflection_element.html'
    fields = ['name', 'description', 'question']
    success_url = reverse_lazy('reflection_elements')


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
    success_url = reverse_lazy('html_elements')


class EditReflectionElement(UpdateView):
    model = Reflection
    template_name = 'reflection_element.html'
    fields = ['name', 'description', 'question']
    success_url = reverse_lazy('reflection_elements')