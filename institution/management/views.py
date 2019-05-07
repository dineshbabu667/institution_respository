from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers  import reverse

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.contrib import messages

from datetime import date
import datetime

from django_tables2 import RequestConfig
from decimal import getcontext, Decimal
from crispy_forms.layout import Submit,ButtonHolder,Reset

from django.contrib.auth.models import User,Group
from management.models import Student,Courses,Group,AssignGroupDetail

from management.forms import StudentAddMultiForm,CourseAddform,GroupAddform
from management.tables import Course_Table,Group_Table,AssignGroupDetail_Table,AssignGroupDetailFilter,AssignGroupDetail_Search_Form


class CourseAdd(CreateView):
    form_class = CourseAddform
    template_name = 'management/generic_add.html'
    
    def get_context_data(self, **kwargs):
       context = super(CourseAdd, self).get_context_data(**kwargs)
       context['Title'] = 'Add Course'
       context['Listtitle'] ='List Courses'
       
       course_qs = Courses.objects.all()
       CourseTable = Course_Table(course_qs)
       context['table'] = CourseTable
       return context
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Course Added Successfully')
        return reverse("management:courseadd")

class GroupAdd(CreateView):
    form_class = GroupAddform
    template_name = 'management/generic_add.html'
    
    def get_context_data(self, **kwargs):
       context = super(GroupAdd, self).get_context_data(**kwargs)
       context['Title'] = 'Add Group'
       context['Listtitle'] ='List Groups'
       
       group_qs = Group.objects.all()
       GroupTable = Group_Table(group_qs)
       context['table'] = GroupTable
       return context
    def form_valid(self, form):
        #import ipdb;ipdb.set_trace()
        form.instance.created_by_id  = self.request.user.id
        form.instance.created_on   = datetime.datetime.now()
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Group Created successfully.')
        return HttpResponseRedirect(reverse('management:groupadd'))
    
def assign_student(request):
    if request.method == 'POST':
        pass
    else:
        context={} 
        
        #import ipdb;ipdb.set_trace()
        group_qs = Group.objects.all().order_by('group_name')
        student_qs =Student.objects.all().order_by('id')
        
        
       
        context={
             'Title':'Assign Student',
             'group_qs':group_qs,
             'student_qs':student_qs,
                     
            } 
        
        return render(request, 'management/assign_student.html', context)   



def student_landing(request):
    print(request.user.student_user.id)
    assign_group_qs = AssignGroupDetail.objects.filter(assign_student=request.user.student_user.id)
    
    
    context={
             'Title':'Student Group List',
             'assign_group_qs':assign_group_qs,
             'student_id':request.user.student_user.id,
            } 
   
    return render(request,'management/student_landing.html',context)


class ListAssignGroupDetail(ListView):
    #import ipdb;ipdb.set_trace()
    model = AssignGroupDetail
    template_name = 'management/staff_landing.html'
    def get_queryset(self, **kwargs):
        group = Group.objects.filter(created_by=self.request.user)
        return AssignGroupDetail.objects.filter(assign_group_pk__in=group)
    
    def get_context_data(self,**kwargs):
        context=super(ListAssignGroupDetail, self).get_context_data(**kwargs)
        context['Title'] = 'Assign Student List'
        filter = AssignGroupDetailFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = AssignGroupDetail_Search_Form()
        filter.form.helper.add_input(Submit('submit', 'Search',css_class="btn btn-default"))
        filter.form.helper.add_input(Reset('Clear', 'Clear',css_class="btn btn-default",css_id='reset-billid-clear'))
        filter.form.helper.add_input(Reset('Reset Search','Reset Search',css_class="btn btn-default",css_id='reset-search'))
        Table = AssignGroupDetail_Table(filter.qs)
        RequestConfig(self.request, paginate={'per_page': 20}).configure(Table)
        context['table'] = Table
        context['filter'] = filter
        context['Reset_url'] = 'management:stafflanding'
      
        return context  


def assign_student_comments(request,id):
    if request.method == 'POST':
        pass
    else:
        context={} 
        assign_group_detail = AssignGroupDetail.objects.get(id=id )
       
        context={
             'Title':'Student Comments',
             'assign_group_detail':assign_group_detail,
           
                     
            } 
        
        return render(request, 'management/assign_student_comments.html', context) 




def assign_staff_comments(request,id):
    if request.method == 'POST':
        pass
    else:
        context={} 
        
        
        assign_group_detail = AssignGroupDetail.objects.get(id=id )
       
        context={
             'Title':'Staff Comments',
             'assign_group_detail':assign_group_detail,
             
                     
            } 
        
        return render(request, 'management/assign_staff_comments.html', context)



'''

def staff_landing(request):
   
    
    assignstudent_qs  = AssignGroupDetail.objects.all()   
    print(assignstudent_qs)    
    assignstudent_table = AssignGroupDetail_Table(assignstudent_qs)
        
    context={
             'Title':'Assign Student List',
             'table':assignstudent_table,
             
            }             
                
    
    return render(request,'management/staff_landing.html',context)
'''

# Create your views here.
