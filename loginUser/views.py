from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from loginUser.models import MyUser
from loginUser.forms import UserCreationForm
from django.urls import reverse


class RegisterUser(CreateView):
    model = MyUser
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(RegisterUser, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ListUser(ListView):
    model = MyUser
    context_object_name = 'users'
    template_name = 'user_list.html'


class EditUser(UpdateView):
    model = MyUser
    context_object_name = 'users'
    template_name = 'edit_user.html'
    fields = ['email', 'date_of_birth', 'first_name', 'last_name', 'address']

    def get_success_url(self):
        return reverse('users')


class VerifyUser(UpdateView):
    model = MyUser
    context_object_name = 'users'
    fields = ['is_verified']

    def get_success_url(self):
        return reverse('users')


class SuspendUser(UpdateView):
    model = MyUser
    fields = ['is_active']

    def get_success_url(self):
        return reverse('users')


class DeleteUser(DeleteView):
    model = MyUser

    def get_success_url(self):
        return reverse('users')
