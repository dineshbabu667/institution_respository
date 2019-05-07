import django_tables2 as tables
from django_tables2.utils import A

from datetime import date
from django.db.models import Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

import django_filters 
from django_filters import DateRangeFilter,DateFilter

from django.template.defaultfilters import date

from management.models import Student,Courses,Group,AssignGroupDetail

class Course_Table(tables.Table):
   
   
    class Meta:
         model =  Courses
         orderable = True
         attrs = {'class': 'table table-striped table-bordered table-hover','id':'Table_list'}
         fields=['course_name','created_on','modified_on']
         
         

class Group_Table(tables.Table):
   
   
    class Meta:
         model =  Group
         orderable = True
         attrs = {'class': 'table table-striped table-bordered table-hover','id':'Table_list'}
         fields=['group_name','created_by','created_on','modified_on']
 
 
class AssignGroupDetail_Table(tables.Table):
   
   
    BUTTON_TEMPLATE = """ 
    {% if record.assign_student_status == 1 %}
    
        <a href="{% url 'management:staffcomments' record.id %}" class="btn btn-primary">Comments</a>
        &nbsp;&nbsp;
         <a href="#" class="btn btn-danger block_btn" id="id-{{record.id}}-block_btn" rel="{{record.id}}">Block</a>
          &nbsp;&nbsp;
    {% endif %} 
    {% if  record.assign_student_status == 2 %}   
         <a href="#" class="btn btn-warning unblock_btn" id="id-{{record.id}}-unblock_btn" rel="{{record.id}}">UnBlock</a>
    {% endif %}    
     {% if  record.assign_student_status == 0 %}    
             <div id="id-{{record.id}}-assign_comments" style="display:none;">
                 <a href="{% url 'management:staffcomments' record.id %}" class="btn btn-primary">Comments</a>
             </div>
             <div id="id-{{record.id}}-assign_request" style="display:show;">
                 <a href="#" class="btn btn-info">Request Sent</a>
             </div>
     {%endif %}
     
    """
    # <a href="{% url 'Invoice:invoicecancel' record.id  %}" data-toggle="confirmation" data-original-title="Cancel! Are you sure ?"  title=""> <i class="fa fa-ban" aria-hidden="true" title="Cancel"></i></a>
    Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
   
   
   
   
   
    class Meta:
         model =  AssignGroupDetail
         orderable = True
         attrs = {'class': 'table table-striped table-bordered table-hover','id':'Table_list'}
         fields=['assign_group_pk','assign_student','created_on','modified_on']   
         
         
         
class AssignGroupDetailFilter(django_filters.FilterSet):
    
    created_min = django_filters.DateFilter(name='created_on', lookup_expr='gte',label='From Date')
    created_max = django_filters.DateFilter(name='created_on', lookup_expr='lte',label='To Date')
   
    
   
    class Meta:
        model =AssignGroupDetail
        fields=['assign_group_pk','assign_student','assign_student_status']
       
class AssignGroupDetail_Search_Form(FormHelper):
    
        model = AssignGroupDetail
        form_id = 'Search_Form'
        form_method = 'get'
        form_class = 'form-horizontal'
        form_role = 'form'
        label_class = 'col-md-3'
        field_class = 'col-md-5'