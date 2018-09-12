"""Elearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'user_api', views.UserViewSet)
router.register(r'courses_api', views.GroupsCoursesViewSet, base_name='courses_api')
router.register(r'chapters_api/(?P<course_id>\d+)', views.ChaptersViewSet, base_name='chapters_api')
router.register(r'chapters_api', views.ChaptersViewSet, base_name='chapters_api')
router.register(r'elements_api/(?P<chapter_id>\d+)', views.ElementViewSet, base_name='elements_api')
router.register(r'elements_api', views.ElementViewSet, base_name='elements_api')
router.register(r'tei_api/(?P<element_id>\d+)', views.TEIViewSet, base_name='tei_api')

urlpatterns = [
    path('', include('student.urls', namespace='student')),
    path('', include('loginUser.urls')),
    path('', include('courseware.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
