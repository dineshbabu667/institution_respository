from django.contrib import admin
from management.models import Courses,Student,Group,AssignGroup,AssignGroupDetail
# Register your models here.
admin.site.register(Courses)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(AssignGroup)
admin.site.register(AssignGroupDetail)