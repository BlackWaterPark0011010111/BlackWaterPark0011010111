from django.shortcuts import render

# Create your views here.

def blog_home(req): 
    return render(req, 'home.html')