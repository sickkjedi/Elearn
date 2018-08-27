from rest_framework import serializers

from loginUser.models import MyUser
from courseware.models import Groups, Courses


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
