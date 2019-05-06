
from django.conf.urls import include, url
 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
 
from . import views
 
from .views import AssignGroupCreateview,AssignGroupList,AssignGroupShowList, GroupCreateview
from .views import AssignGroupRudview,StudentGroupComments,StudentGroupCommentList
from .views import StaffGroupComments,StaffGroupCommentList
from .views import BlockStudentRudview

assigngroupview = AssignGroupCreateview.as_view(
                {
                    'get': 'list',
                    'post': 'create'
                }
                )

assigngroupuplist = AssignGroupList.as_view(
                {
                    'get': 'list',
                }
                )
'''
assigngroupupshowlist = AssignGroupShowList.as_view(
                {
                    'get': 'list',
                }
                )
'''
urlpatterns = [
           
            #url(r'^assignstudentapi/$', AssignGroupCreateview.as_view(), name='assignstudentapi'),
            
            url(r'^assignstudentapi/$', assigngroupview  , name='assignstudentapi'), 
            url(r'^assigngrouplistapi/$', assigngroupuplist  , name='assigngrouplistapi'), 
            url(r'^groupshowapi/$', AssignGroupShowList.as_view(), name='groupshowapi'),
            url(r'^updatestatusapi/(?P<pk>[0-9]+)/$', AssignGroupRudview.as_view(), name='updatestatusapi'), 
            url(r'^studentcomments/$', StudentGroupComments.as_view(), name='studentcomments'),
            url(r'^studentcommentlist/$', StudentGroupCommentList.as_view(), name='studentcommentlist'),
            url(r'^staffcomment/$', StaffGroupComments.as_view(), name='staffcomment'),
            url(r'^staffcommentlist/$', StaffGroupCommentList.as_view(), name='staffcommentlist'),
            url(r'^studentblockapi/(?P<pk>[0-9]+)/$', BlockStudentRudview.as_view(), name='studentblockapi'), 
            
            
                 
            url(r'^groupapi/$', GroupCreateview.as_view(), name='groupapi'),
            
            
]