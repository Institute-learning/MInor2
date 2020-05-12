from django.contrib import admin

from .models import Course,Module,studyMat,quiz,question



admin.site.register(Course)
admin.site.register(Module)
admin.site.register(studyMat)
admin.site.register(quiz)
admin.site.register(question)
