from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request,'Ins/dashboard.html')

def erreichte_Konten(request):
    return render(request,'Ins/Erreichte_Konten.html')

def content_Interaktionen(request):
    return render(request ,'Ins/Content-Interaktionen.html')