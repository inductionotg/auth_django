from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testApp/home.html')

def java_exams_view(request):
    return render(request,'testApp/javaexams.html')

def python_exams_view(request):
    return render(request,'testApp/pythonexams.html')

def apti_exams_view(request):
    return render(request,'testApp/aptiexams.html')
