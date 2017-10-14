from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import misaka
from simplesocial.settings import MEDIA_DIR
import os,errno



from groups.models import Group

from django.contrib.auth import get_user_model



# Create your models here.

User=get_user_model()

def user_directory_path(instance,filename):
    try:
        
        print('###################',os.path.join(MEDIA_DIR,instance.user.username))
        os.makedirs(os.path.join(MEDIA_DIR,instance.user.username))
        
    
    except OSError as e:
        if e.errno!=errno.EEXIST:
            raise
        
    return instance.user.username+'/'+filename

class Post(models.Model):
    
    user = models.ForeignKey(User,related_name='posts')
    created_at=models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group =models.ForeignKey(Group,related_name='posts',null=True,blank=True)
    custom_viz = models.TextField(blank=True)
    #custom_viz_html= models.TextField(editable=False,blank=True)
    
    data_file = models.FileField(upload_to=user_directory_path, blank=True)
    
    
    
    
    def __str__(self):
        return self.message
    
    
    def save(self,*args,**kwargs):
        #self.custom_viz_html = self.custom_viz
        self.message_html = misaka.html(self.message,extensions=('tables','fence-code',))
        super(Post,self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
    
    
    class Meta:
        ordering =['-created_at']
        unique_together =['user','message']
        
        
