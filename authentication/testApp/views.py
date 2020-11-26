from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testApp/home.html')

def java_exams_view(request):
    return render(request,'testApp/javaexams.html')
    
