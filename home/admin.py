from django.contrib import admin

from .models import Student,StudyFolder,Subject,Instructor,Course,Module,Quiz,QuizResult,ReadyQuiz,Destination

#admin.site.register(Institute)
#admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(StudyFolder)
admin.site.register(Subject)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Destination)

admin.site.register(Quiz)
admin.site.register(QuizResult)
admin.site.register(ReadyQuiz)
