from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.
def home(req):
    form = UserForm()
    return render(req, template_name='index.html', context={'myForm': form})


def new_user(req): 
    if req.method == 'POST': 
        form = UserForm(req.POST)
        
        if form.is_valid(): 
            new_user = form.cleaned_data
            User.objects.create(**new_user)
            
    
    form = UserForm()
    return render(req, template_name='index.html', context={'myForm': form})
 
            
            
            
        


