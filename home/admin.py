from django.contrib import admin

from .models import Course,Module,quiz,question,student1,studyMat,cart,scorecard



admin.site.register(Course)
admin.site.register(Module)
admin.site.register(studyMat)
admin.site.register(quiz)
admin.site.register(question)
admin.site.register(student1)
admin.site.register(cart)
admin.site.register(scorecard)
