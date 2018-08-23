from rest_framework import serializers

from loginUser.models import MyUser
from courseware.models import Groups, Courses


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'first_name', 'last_name', 'address')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groups
        fields = ('group_name', 'description')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('course_name', 'description')
