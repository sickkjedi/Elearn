from rest_framework import serializers

from loginUser.models import MyUser
from courseware.models import Groups, Courses, Chapters, HtmlTE, Reflection, TeachingElementBase


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'date_of_birth', 'first_name', 'last_name', 'address')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('id', 'course_name', 'description')


class GroupSerializer(serializers.ModelSerializer):
    courses_set = CourseSerializer(many=True)

    class Meta(object):
        model = Groups
        fields = ('id', 'group_name', 'description', 'courses_set')


class ChapterSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Chapters
        fields = ('name', 'id')


class TEISerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachingElementBase
        fields = ['name', 'description', 'te_type']


class HtmlTESerializer(serializers.ModelSerializer):

    class Meta:
        model = HtmlTE
        fields = ('name', 'description', 'html')


class ReflectionTESerializer(serializers.ModelSerializer):

    class Meta:
        model = Reflection
        fields = ('name', 'description', 'question')


