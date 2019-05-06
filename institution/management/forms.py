from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets 
from betterforms.multiform import MultiModelForm

from django.contrib.auth.models import User,Group
from management.models import Student,Courses,Group,AssignGroup,AssignGroupDetail
from django.contrib.auth.forms import UserCreationForm



class StudentUserAddForm(UserCreationForm):
    
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.CharField(required = True)
    
    class Meta:
        model= User
        fields=[ 'first_name', 'last_name', 'email','username','password1', 'password2',]
        exclude=['is_staff']





class StudentAddform(forms.ModelForm):
    
    class Meta:
        model= Student
        fields='__all__'
        exclude=['created_on','modified_on','user']
        
        

class StudentAddMultiForm(MultiModelForm):
    form_classes = {
        'form1': StudentUserAddForm,
        'form2': StudentAddform,
        
        }
    
    
class CourseAddform(forms.ModelForm):
    
    class Meta:
        model= Courses
        fields='__all__'
        exclude=['created_on','modified_on',]
        

class GroupAddform(forms.ModelForm):
    
    class Meta:
        model= Group
        fields=['course','group_name']
        exclude=['created_by','created_on','modified_on','status']
        

        
       


     
