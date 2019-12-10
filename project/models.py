# Create your models here.
from datetime import datetime, timedelta
from django.db import models
from django.urls import reverse #to obtain url 

#Create your models here.

class Laptop(models.Model):
    '''encapsulate the idea of a laptop:'''

    #data attributes of a Laptop:
    model_name = models.TextField(blank = True)
    model_id = models.TextField(blank = True)
    cost = models.TextField(blank = True)
    model_url = models.URLField(blank = True)

    def __str__(self):
        '''return in string format of the object'''
        return '%s, %s ,%s' % (self.model_name , self.model_id, self.cost)

    
    def get_absolute_url(self):
        '''return a URL to display this RENTAL PAGE.'''
        return reverse("show_all_rental_page")

    # get reviews/inquiry of this laptop
    def get_reviews(self):
        '''return a QuerySet of all messages for this laptop.'''
        result = Review.objects.filter(laptop = self.pk)
        return result


class Profile(models.Model):
    '''encapsulate the idea of a mini_fb:'''

    #data attributes of a mini_fb:
    name = models.TextField(blank = True)
    student_id = models.TextField(blank = True)
    email = models.TextField(blank = True)
    phone = models.TextField(blank = True)
    dateIn = models.DateField(default = datetime.now())
    dateOut = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    laptop = models.ForeignKey('Laptop',on_delete = "CASCADE")


    def __str__(self):
        '''return in string format of the object'''
        return '%s, %s ,%s ,%s' % (self.name, self.student_id ,self.email,self.phone)

    def get_absolute_url(self):
        '''return a URL to display this profile object.'''
        return reverse("show_profile_page",kwargs ={"pk": self.pk})



class Review(models.Model):
    '''encapsulate the review'''

    #data attributes of a mini_fb:
    timestamp = models.DateField(default = datetime.now())
    comment = models.TextField(blank = True)
    person = models.TextField(blank = True)
    laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)

    def ___str___(self):
        '''return a string representation of this object.'''
        return '"%s" - %s' % (self.timestamp, self.comment)
