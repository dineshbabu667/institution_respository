from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
app_name = 'management'

from . import views

from .views import CourseAdd,GroupAdd,ListAssignGroupDetail

urlpatterns = [
            
           url(r'^(?i)courseadd', login_required(CourseAdd.as_view()), name='courseadd'),
           url(r'^(?i)groupadd', login_required(GroupAdd.as_view()), name='groupadd'),
           
           url(r'^(?i)stafflanding', login_required(ListAssignGroupDetail.as_view()), name='stafflanding'),
           url(r'^(?i)studentlanding', login_required(views.student_landing), name='studentlanding'),
           url(r'^(?i)assignstudent', login_required(views.assign_student), name='assignstudent'),
           
           url(r'^(?i)studentscomments/(?P<id>[-\w]+)/$', login_required(views.assign_student_comments), name='studentscomments'),
           
            url(r'^(?i)staffcomments/(?P<id>[-\w]+)/$', login_required(views.assign_staff_comments), name='staffcomments'), 
            
]          