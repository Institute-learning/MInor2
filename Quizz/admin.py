from django.contrib import admin

from .models import Institute,Batch,Student,StudyFolder,Subject,Instructor,Quiz,QuizResult,ReadyQuiz

admin.site.register(Institute)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(StudyFolder)
admin.site.register(Subject)
admin.site.register(Instructor)
admin.site.register(Quiz)
admin.site.register(QuizResult)
admin.site.register(ReadyQuiz)