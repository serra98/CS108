
# Create your models here.
from django.db import models
from django.urls import reverse #to obtain url 

#Create your models here.
#first name, last name, email address, and a profile image url 

class Profile(models.Model):
    '''encapsulate the idea of a mini_fb:'''

    #data attributes of a mini_fb:
    first_name = models.TextField(blank = True)
    last_name = models.TextField(blank = True)
    home_town = models.TextField(blank = True)
    email = models.TextField(blank = True)
    prof_url = models.URLField(blank = True)

    def __str__(self):
        '''return in string format of the object'''
        return '%s, %s ,%s' % (self.first_name , self.last_name, self.home_town)

    
    # get status message of this profile 
    def get_status_messages(self):
        '''return a QuerySet of all messages for this profile.'''
        result = StatusMessage.objects.filter(profile = self.pk)
        return result

    def get_absolute_url(self):
        '''return a URL to display this profile object.'''
        return reverse("show_profile_page",kwargs ={"pk": self.pk})

class StatusMessage(models.Model):
    '''encapsulate the statusmessage'''

    #data attributes of a mini_fb:
    timestamp = models.TimeField(blank = True,auto_now = True)
    message = models.TextField(blank = True)
    profile = models.ForeignKey('Profile', on_delete="CASCADE")

    def ___str___(self):
        '''return a string representation of this object.'''
        return '"%s" - %s' % (self.timestamp, self.message)

