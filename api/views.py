from rest_framework import viewsets

from loginUser.models import MyUser
from courseware.models import Groups
from api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return MyUser.objects.filter(id=user_id)


class GroupsCoursesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows courses and groups to be viewed.
    """
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Groups.objects.filter(users__id=user_id)
