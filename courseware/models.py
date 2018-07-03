from django.db import models
from loginUser import models as user_models


class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default='')
    year = models.SmallIntegerField(default=0)
    users = models.ManyToManyField(user_models.MyUser)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('group_name',)


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default='')
    teacher = models.CharField(max_length=50, default='')
    groups = models.ManyToManyField(Groups)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ('course_name',)


class TeachingElementBase(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE, default=None)
    chapter = models.ForeignKey("Chapters", on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name


class HtmlTE(TeachingElementBase):
    type = models.CharField(default='HTML', max_length=20)
    html = models.TextField()


class Reflection(TeachingElementBase):
    type = models.CharField(default='Reflection', max_length=20)
    question = models.CharField(max_length=255)


class Chapters(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey("Courses", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


