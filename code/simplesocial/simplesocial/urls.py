"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django import views as dj_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^accounts/',include('accounts.urls', namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')), # additional stuff to enable auth views connection?
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^posts/',include('posts.urls', namespace='posts')),
    url(r'^groups/',include('groups.urls', namespace='groups')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
                 
                 
                url(r'^__debug__/',include(debug_toolbar.urls)),
                url(r'^admin/', admin.site.urls),
                url(r'^$',views.HomePage.as_view(),name='home'),
                url(r'^accounts/',include('accounts.urls', namespace='accounts')),
                url(r'^accounts/',include('django.contrib.auth.urls')), # additional stuff to enable auth views connection?
                url(r'^test/$',views.TestPage.as_view(),name='test'),
                url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
                url(r'^posts/',include('posts.urls', namespace='posts')),
                url(r'^groups/',include('groups.urls', namespace='groups')),
                url(r'^media/(?P<path>.*)$', dj_views.static.serve, {'document_root': settings.MEDIA_ROOT,}),
                url(r'^static/(?P<path>.*)$', dj_views.static.serve, {'document_root': settings.STATIC_ROOT,}), 
                
                 ]