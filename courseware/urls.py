from django.urls import path
from django.views import i18n
from django.conf.urls import url

from . import views

urlpatterns = [
    path('groups', views.ListGroups.as_view(), name='groups'),
    path('groups/add_group', views.AddGroup.as_view(), name='add_group'),
    path('groups/edit_group/<int:pk>', views.EditGroup.as_view(), name='edit_group'),
    path('courses', views.ListCourses.as_view(), name='courses'),
    path('courses/add_course', views.AddCourse.as_view(), name='add_course'),
    path('courses/edit_course/<int:pk>', views.EditCourse.as_view(), name='edit_course'),
    url(r'^admin/jsi18n/$', i18n.null_javascript_catalog, name='jsi18n'),
]