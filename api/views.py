from rest_framework import viewsets

from loginUser.models import MyUser
from courseware.models import Groups, Chapters
from api.serializers import UserSerializer, GroupSerializer, ChapterSerializer


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


class ChaptersElementsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows chapters and elements to be viewed.
    """
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_pk = self.kwargs.get('course_id')
        query = {"course_id": course_pk} if course_pk else {}
        return Chapters.objects.filter(**query)
