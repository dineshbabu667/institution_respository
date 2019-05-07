from rest_framework import serializers

from django.contrib.auth.models import User

from management.models import AssignGroup,AssignGroupDetail,Group,Student,AssignGroupComments
from lib2to3.pgen2.tokenize import group



class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('group_name','created_by' )

        

class AssignGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignGroup
        fields = ('group', 'status', )
       

class AssignGroupDetailSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = AssignGroupDetail
        fields = ('assign_group_pk', 'assign_student_id', )  
    
    


class AssignGroupListSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = AssignGroupDetail
        fields = ('assign_student_status', )  

class StudentCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignGroupComments
        fields = ('assign_group_pk','assign_group_detail', 'message' )

class StudentCommentsListSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y -%m -%d')
    #groupname = serializers.ReadOnlyField(source='assign_group_pk.group_name')
    student_name = serializers.ReadOnlyField()
    staff_name = serializers.ReadOnlyField(source='group_created_by.username')
    class Meta:
        model = AssignGroupComments
        fields = ('assign_group_pk','assign_group_detail','group_created_by','student_name','staff_name','message','created_on' )

class StaffCommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssignGroupComments
        fields = ('assign_group_pk','group_created_by', 'message', )

class StaffCommentsListSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y -%m -%d')
    student_name = serializers.ReadOnlyField()
    staff_name = serializers.ReadOnlyField(source='group_created_by.username')
    class Meta:
        model = AssignGroupComments
        fields = ('assign_group_pk','assign_group_detail','group_created_by','student_name','staff_name', 'message', 'created_on')



class AssignGroupReadStatusSerializer(serializers.ModelSerializer):
    
    student_name = serializers.ReadOnlyField(source='assign_student.user.username')
    groupname = serializers.ReadOnlyField(source='assign_group_pk.group_name')
    class Meta:
        model = AssignGroupDetail
        fields = ('id','assign_group_pk','assign_student','groupname','student_name','assign_student_status','read_status' )  


class StaffupdatereadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssignGroupDetail
        fields = ('read_status', ) 


class StudentGroupDetailSerializer(serializers.ModelSerializer):
  
    groupname = serializers.ReadOnlyField(source='assign_group_pk.group_name')
    class Meta:
        model = AssignGroupDetail
        fields = ('assign_group_pk', 'assign_student_id','groupname','created_on' )  





       
     
class AssignListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data):
        assign_group = [AssignGroupDetail(**item) for item in validated_data]
        return AssignGroupDetail.objects.bulk_create(assign_group)

class AssignSerializer(serializers.Serializer):
    assign_group_pk = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    assign_student = serializers.PrimaryKeyRelatedField(queryset =Student.objects.all())
    
   
    def create(self, validated_data):
        assign_group = [AssignGroupDetail(**item) for item in validated_data]
        return AssignGroupDetail.objects.bulk_create(assign_group)    
 

        
        
        
     
