from django.contrib import admin
from .models import Course, Project, Workshop, Feedback, Contact, Callme, Photos,About, Carousal, Registerfirst

# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback')


admin.site.register(Course)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Callme)
admin.site.register(Contact)
admin.site.register(Photos)
admin.site.register(About)
admin.site.register(Carousal)
admin.site.register(Registerfirst)





