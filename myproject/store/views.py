from django.shortcuts import render

# Create your views here.
def index(request):
    index = index.objects.all()
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def resume(request):
    return render(request,'resume.html')