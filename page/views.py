from django.shortcuts import render
from . import views

# Create your views here.
def home(request):

    return render(request,'page/home.html')

def about(request):
    
    return render(request,'page/about.html')

def contact(request):
    
    return render(request,'page/contact.html')