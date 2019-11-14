from django.shortcuts import render

# Create your views here.
from .models import Quote , Person
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    '''create a subclass of ListView to display all quotes.'''

    model = Quote #retrieve objects of type Quote from database 
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    '''show one quote'''

    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    ''' show one quote selected at random.'''
    model = Quote 
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    #pick one quote at random 
    def get_object(self):
        '''return a single instance of a quote object, selected at random.'''
        # get all quotes 
        all_quotes = Quote.objects.all() 
        # pick one, at random 
        r = random.randint(0,len(all_quotes) -1)
        q = all_quotes[r]
        return q


class PersonPageView(DetailView):
    '''show all quotes and all images for one person.'''

    model = Person 
    template_name = 'quotes/person.html'
    context_object_name = 'person'
