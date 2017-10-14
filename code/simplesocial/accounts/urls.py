from django.conf.urls import url
from django.contrib.auth import views as auth_views #django 1.11 has included login and log out views
from . import views

app_name='accounts'

urlpatterns=[
             url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
             url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),# there is already a default page set up...home?
             url(r'signup/$',views.SignUp.as_view(),name='signup'),
             ]