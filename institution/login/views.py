from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers  import reverse

from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



from django.contrib.auth.models import User,Group
from management.models import Student

from management.forms import StudentAddMultiForm


# Create your views here.
def home(request):
    return render(request,'login/index.html')




def staff_landing(request):
    return render(request,'login/landing.html')




class RegisterStudent(CreateView):
    
    form_class = StudentAddMultiForm
    template_name = 'login/student_register.html'
    def get_context_data(self, **kwargs):
       context = super(RegisterStudent, self).get_context_data(**kwargs)
       context['Title'] = 'Register Student'
       return context
    
    
    def form_valid(self, form):
        form1 = form['form1']
        form2 = form['form2']
        raw_password = form.cleaned_data.get('form1-password1')
        user_form = form1.save()
        user_form.refresh_from_db()
        user_id=user_form.id
        form2.instance.user = user_form
        form2.save()
        request.session['customer_login'] ='customer_login'        
        user = auth.authenticate(username=user_form.username, password=raw_password)
        auth.login(self.request, user_form)
       
        return HttpResponseRedirect('/studentlanding/',)
    
    
def student_login(request):
    
    username= request.POST.get('username')
    password = request.POST.get('password')
    
    try:
        findUser = username
    except User.DoesNotExist:
        findUser = None
        
    if findUser is not None:
        caseSensitiveUsername = findUser
        user = auth.authenticate(username=caseSensitiveUsername,password=password)
    else:
        user = None
    
            
    request.session['customer_login'] ='customer_login'
   
        
    if user is not None:
        auth.login(request,user) 
        
        return HttpResponseRedirect('/studentlanding/',)
        
    else:
        Error_Text = "Login Details are invalid"
        return render(request, 'login/student_login.html',{'Error_Text': Error_Text})
    
    
    
def log_out(request):
    auth.logout(request)
    
    return HttpResponseRedirect('/home/',)






