from django.db import models
from loginUser import models as user_models


class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, default='')
    year = models.SmallIntegerField(default=0)
    users = models.ManyToManyField(user_models.MyUser)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('group_name',)


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, default='')
    teacher = models.CharField(max_length=50, default='')
    groups = models.ManyToManyField(Groups)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ('course_name',)
