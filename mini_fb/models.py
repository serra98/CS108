from django.db import models

# Create your models here.
#first name, lst name, email address, and a profile image url 


class mini_fb(models.Model):
    '''encapsulate the idea of a mini_fb:'''

    #data attributes of a mini_fb:
    first_name = models.TextField(blank = True)
    last_name = models.TextField(blank = True)
    home_town = models.TextField(blank = True)
    email = models.TextField(blank = True)
    prof_url = models.URLField(blank = True)

def __str__(self):
    '''return in string format of the object'''
    return '"%s" - %s' % (self.first_name , self.last_name,self.home_town)
