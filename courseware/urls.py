from django.urls import path, include
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

    path('courses/chapters/<int:pk>/elements', views.ListElements.as_view(), name='elements'),
    path('courses/chapters/<int:pk>/elements/html', views.ListHtmlElements.as_view(), name='html_elements'),
    path('courses/chapters/<int:pk>/elements/add_html', views.AddHtmlElement.as_view(), name='add_html_element'),
    path('courses/chapters/elements/html/edit_element/<int:pk>', views.EditHTMLElement.as_view(), name='edit_html_element'),
    path('courses/chapters/<int:pk>/elements/reflection', views.ListReflectionElements.as_view(), name='reflection_elements'),
    path('courses/chapters/<int:pk>/elements/add_reflection', views.AddReflectionElement.as_view(), name='add_reflection_element'),
    path('courses/chapters/elements/reflection/edit_element/<int:pk>', views.EditReflectionElement.as_view(), name='edit_reflection_element'),

    path('courses/edit_course/<int:pk>/chapters', views.ListChapters.as_view(), name='chapters'),
    path('courses/edit_course/<int:pk>/chapters/add_chapter', views.AddChapter.as_view(), name='add_chapter'),
    path('courses/edit_course/chapters/edit_chapter/<int:pk>', views.EditChapter.as_view(), name='edit_chapter'),

    url(r'^admin/jsi18n/$', i18n.null_javascript_catalog, name='jsi18n'),
]