from __future__ import unicode_literals
from django.shortcuts import render
# import generics
from rest_framework import generics
#import apiview
from rest_framework.views import APIView
# Response
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from rest_framework.permissions import IsAuthenticated,AllowAny,SAFE_METHODS,IsAuthenticatedOrReadOnly
from rest_framework import permissions

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.db.models import Q

#import models
from management.models import Student,Courses,Group,AssignGroup,AssignGroupDetail,AssignGroupComments

# serializer
from management.api.serializers import AssignGroupSerializer, GroupSerializer, AssignGroupDetailSerializer
from management.api.serializers import AssignSerializer,AssignGroupListSerializer,StudentCommentsSerializer
from management.api.serializers import StaffCommentsSerializer



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)




class AssignGroupCreateview(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AssignGroupDetailSerializer
    queryset = AssignGroupDetail.objects.all() 
    
    def create(self, request, *args, **kwargs):
        #import ipdb;ipdb.set_trace()
        #serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        #serializer.is_valid(raise_exception=True)
        data=request.data
        print(data)
        assign_group = data['assign_group_pk']
        assign_student = data['assign_student_id']
        
        for item in assign_student: 
            AssignGroupDetail.objects.create(assign_group_pk_id = assign_group, assign_student_id=item)
        #self.perform_create(serializer)
        headers = self.get_success_headers(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)


class AssignGroupList(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()
   
    
    def list(self, request):
        queryset =  AssignGroupDetail.objects.all()
        serializer = AssignGroupListSerializer(queryset, many=True)
        return Response(serializer.data)


class AssignGroupRudview(generics.RetrieveUpdateDestroyAPIView):
    lookup_field= 'pk'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AssignGroupListSerializer
    def get_queryset(self):
        return AssignGroupDetail.objects.all()



class StudentGroupComments(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = StudentCommentsSerializer
    queryset = AssignGroupComments.objects.all()

class StudentGroupCommentList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = StudentCommentsSerializer
    queryset = AssignGroupComments.objects.all()

class StaffGroupCommentList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = StaffCommentsSerializer
    queryset = AssignGroupComments.objects.all()



class AssignGroupShowList(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AssignGroupListSerializer

    
    
 
    
    
class GroupCreateview(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    

        
