from . import views
from django.urls import path

app_name = 'student'

urlpatterns = [
    path('home', views.StudentHome.as_view(), name='student_home')
]