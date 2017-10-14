from django.contrib.auth import get_user_model #returns usr model that is currently active in this project
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields =('username','email','password1','password2')
        model= get_user_model() #connecting with current user's object'
        
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs) #initializing parent class to access its attributes
            self.fields['username'].label ='Display Name' # setting up the label that will be rendered in html
            self.fields['email'].label = 'Email Address'
            #try for password1&2 change to password and confirm?