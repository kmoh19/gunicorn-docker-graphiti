from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class =forms.UserCreateForm # note how class is assigned NOT instance of class as in UsercreateForm()
    success_url= reverse_lazy('login')
    template_name='accounts/signup.html'
