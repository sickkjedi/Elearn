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
    course = models.ForeignKey("Courses", on_delete=models.CASCADE)
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
    order_id = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = self.__class__.objects.filter(order_id=self.order_id).aggregate(largest=models.Max('order_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.order_id = last_id + 1

        super(Chapters, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


