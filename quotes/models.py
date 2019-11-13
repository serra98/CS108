from django.db import models
from django.urls import reverse 

import random

# Create your models here.

class Person(models.Model):
    '''encapsulate the concept of a person, who said some famous quote.'''
    name = models.TextField(blank =False)

    def __str__(self):
        '''return a string representation of this object.'''
        return self.name 
    
    def get_random_image(self):
        '''return an image of this person, chosen at random.'''

        #get all images of this person 
        images = Image.objects.filter(person=self.pk)

        i = random.randint(0, len(images) -1)
        return images[i]
    
    def get_all_images(self):
        '''return all QuerySet of all images for this person.'''

        #get all images of this person 
        images = Image.objects.filter(person = self.pk)
        return images 
    
    #get all quotes of this person 
    def get_all_quotes(self): 
        '''return a queryset of all quotes for this person.'''

        #get all quotes of this person 
        quotes = Quote.objects.filter(person = self.pk)
        return quotes 

class Quote(models.Model):
    '''Encapsulate the idea of the quote.'''

    #data attributes of a quote: 
    text = models.TextField(blank = True)
    person =models.ForeignKey('Person', on_delete="CASCADE")
    
    
    def __str__(self):
        '''return a string representation of this object.'''
        return '"%s" - %s' % (self.text, self.person.name)

    def get_absolute_url(self):
        ''''Return a URL to display this quote object.'''
        return reverse("quote",kwargs="pk":self.pk)
class Image(models.Model):
    ''' represent an image which is associated with a person.'''

    image_url = models.URLField(blank = True)
    person = models.ForeignKey('Person',on_delete="CASCADE")

    def __str__(self):
        '''return a string representation of this object.'''
        return self.image_url