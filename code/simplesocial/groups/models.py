from django.db import models
from django.utils.text import slugify #string cleansing so u can use user text input in url definitions
import misaka #enables use of markdowns, embedding?
from django.contrib.auth import get_user_model
from django import template
from django.core.urlresolvers import reverse


# Create your models here.
User =get_user_model() # get current user session

register = template.Library() # for template tagging refer to learning templates exercise basic_app/templatetags
#however it appears to be able to allow the calling of related_name values in template tags......see get_user_groups in post_list.html



class Group(models.Model):
    
    name=models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='')
    description_html=models.TextField(editable=False,default='',blank=True)
    members =models.ManyToManyField(User,through='GroupMember')
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs): #overriding Model save?
        self.slug= slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})
    
    
    class Meta:
        ordering=['name']
        
        

class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships')
    user= models.ForeignKey(User,related_name='user_groups')
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        unique_together =('group','user')# why?---- to prevent duplication