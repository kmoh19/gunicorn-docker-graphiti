from django.contrib import admin
from . import models
# Register your models here.



class GroupMemberInline(admin.TabularInline):# how to display in admin page
    model=models.GroupMember

admin.site.register(models.Group)