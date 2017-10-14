from groups import models
from django import template
from django.contrib.auth import get_user_model

User=get_user_model()
register= template.Library()

@register.simple_tag(takes_context=True,name='user_group_getter')
def user_group_getter(context):
    
    #print(models.GroupMember.objects.filter(user_id=context['user'].pk))
    
    return models.GroupMember.objects.filter(user=context['user'])




@register.simple_tag(takes_context=True)
def all_group_getter(context):
    return models.Group.objects.all()