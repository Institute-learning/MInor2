from django.contrib import admin

from .models import Student,StudyFolder,Course,Module,Quiz,QuizResult,ReadyQuiz,Destination,stud

admin.site.register(stud)
#admin.site.register(Institute)
#admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(StudyFolder)

admin.site.register(Course)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('courseName','courseDesc','courseImage','price','bought')
#     ordering = ('courseName',)
#     search_fields = ('courseName', 'courseDesc')


admin.site.register(Module)
admin.site.register(Destination)

admin.site.register(Quiz)
admin.site.register(QuizResult)
admin.site.register(ReadyQuiz)
