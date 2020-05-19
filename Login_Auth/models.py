from django.db import models
from django.contrib.auth.models import User
from home.models import Course

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolledCourses = models.ManyToManyField(Course,null = True,  blank = True, default=None)

    def __str__(self):
        return self.user.username


