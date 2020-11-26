from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'testApp/home.html')
@login_required
def java_exams_view(request):
    return render(request,'testApp/javaexams.html')

def python_exams_view(request):
    return render(request,'testApp/pythonexams.html')

def apti_exams_view(request):
    return render(request,'testApp/aptiexams.html')

def logout_view(request):
    return render(request,'testApp/logout.html')
