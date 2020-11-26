from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import *
from django.http import HttpResponseRedirect
# Create your views here.
def home_page_view(request):
    return render(request,'testApp/home.html')
@login_required
def java_exams_view(request):
    return render(request,'testApp/javaexams.html')
@login_required
def python_exams_view(request):
    return render(request,'testApp/pythonexams.html')
@login_required
def apti_exams_view(request):
    return render(request,'testApp/aptiexams.html')

def logout_view(request):
    return render(request,'testApp/logout.html')

def sign_up_view(request):
    form=Sign_Up_Form()
    if request.method=='POST':
        form=Sign_Up_Form(request.POST)
        user=form.save()
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})
