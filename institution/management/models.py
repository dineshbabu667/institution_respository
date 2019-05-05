from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from datetime import date

from django.core.urlresolvers import reverse

import os
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg

# Create your models here.


STATUS = (
          (0,'Active'),
          (1,'InActive'),
          (2,'Trash')
          )
ASSIGN_STATUS = (
          (0,'DisConnect'),
          (1,'Connect'),
          (2,'Block')
         
          )

class Student(models.Model):
    user = models.OneToOneField(User,related_name='student_user',on_delete=models.CASCADE)
    mobile_number =  models.CharField(max_length=13,verbose_name='Mobile Number',help_text='Add 10 digits Mobile Number ')
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['id']
        verbose_name = "Student"
        verbose_name_plural = "Students"
        

class Courses(models.Model):
    course_name = models.CharField(max_length=50,verbose_name='Course Name',unique=True)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.course_name
    
    class Meta:
        ordering = ['id']
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Group(models.Model):
    group_name = models.CharField(max_length=50,verbose_name='Group Name',unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_Created_By')
    status =  models.IntegerField(choices=STATUS, default=0,verbose_name='Status')
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.group_name
    
    class Meta:
        ordering = ['id']
        verbose_name = "Group"
        
        
        
class AssignGroup(models.Model):
    group = models.ForeignKey(Group,related_name='assigngroup',verbose_name='Group')
    #student = models.ManyToManyField(Student, verbose_name='Student', related_name='assign_student')
    status =  models.IntegerField(choices=STATUS, default=0,verbose_name='Status')
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        return self.id

class AssignGroupDetail(models.Model):
    assign_group_pk = models.ForeignKey(Group,related_name='assign_group_detail',verbose_name='Assign Group')
    assign_student = models.ForeignKey(Student, verbose_name='Student', related_name='assign_student_detail')
    assign_student_status =  models.IntegerField(choices=ASSIGN_STATUS, default=0,verbose_name='Assign Student Status')
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.created_on)


class AssignGroupComments(models.Model):
    assign_group_pk = models.ForeignKey(Group,related_name='assign_group_comments',verbose_name='Assign Group Comments')
    group_created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_Created_By',blank=True,null=True)
    assign_group_detail = models.ForeignKey(AssignGroupDetail,related_name='assigngroupcomments',verbose_name='Assign Group Comments',blank=True,null=True)
    message = models.TextField(verbose_name= 'Message')
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_on)
       