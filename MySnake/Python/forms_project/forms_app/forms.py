from django import forms  

class UserForm(forms.Form): 
    first_name = forms.CharField(label='first name' )
    last_name = forms.CharField(label = 'last name')
    email = forms.CharField(label= 'email')
    
   