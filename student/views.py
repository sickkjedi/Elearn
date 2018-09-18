from django.views.generic.list import ListView

from loginUser.models import MyUser


class StudentHome(ListView):
    model = MyUser
    context_object_name = 'user'
    template_name = 'student_home.html'
