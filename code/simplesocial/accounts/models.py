from django.db import models
from django.contrib import auth


# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return '@{}'.format(self.username) #username is defined by in the auth.models.User class
