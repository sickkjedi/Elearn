from rest_framework import viewsets

from loginUser.models import MyUser
from courseware.models import Groups, Courses

from api.serializers import UserSerializer, GroupSerializer, CourseSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    # def get_object(self):
    #
    # def get_queryset(self):


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed.
    """
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
