from rest_framework import viewsets

from loginUser.models import MyUser
from courseware.models import Groups, Chapters, TeachingElementBase, HtmlTE, Reflection
from api.serializers import UserSerializer, GroupSerializer, ChapterSerializer, \
    TEISerializer, HtmlTESerializer, ReflectionTESerializer


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


class ChaptersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows chapters to be viewed.
    """
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_pk = self.kwargs.get('course_id')
        query = {"course_id": course_pk} if course_pk else {}
        return Chapters.objects.filter(**query)


class ElementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows elements to be viewed.
    """
    queryset = TeachingElementBase.objects.all()
    serializer_class = TEISerializer

    def get_queryset(self):
        chapter_pk = self.kwargs.get('chapter_id')
        query = {"chapter_id": chapter_pk} if chapter_pk else {}
        return TeachingElementBase.objects.filter(**query)


class TEIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows element data to be viewed.
    """

    queryset = TeachingElementBase.objects.all()
    serializer_class = TEISerializer

    def get_queryset(self):
        def get_te_element(element_id):
            return TeachingElementBase.objects.filter(id=element_id).first().te_type

        element_pk = self.kwargs.get('element_id')
        query = {"id": element_pk} if element_pk else {}

        if get_te_element(element_pk) == 'HTML':
            self.serializer_class = HtmlTESerializer
            return HtmlTE.objects.filter(**query)
        elif get_te_element(element_pk) == 'Reflection':
            self.serializer_class = ReflectionTESerializer
            return Reflection.objects.filter(**query)

