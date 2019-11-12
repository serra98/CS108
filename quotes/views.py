from django.shortcuts import render

# Create your views here.
from .models import Quote 
from django.views.generic import ListView , DetailView 
import random 

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes.'''
    model = Quote #retrieve objects of type Quote from the database 
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    '''show details for on quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'


class RandomQuotePageView(DetailView):
    '''Show one quote selected at random.'''
    model = Quote 
    emplate_name = 'quotes/quote.html'
    context_object_name = 'quote'

    #pick one quote at random 
    def get_object(self):
        '''return a single instance of a Quote object, selected at random.'''

        # get all quotes 
        all_quotes = Quote.objects.all() 

        #pick one at one time 
        r = random.randint(0,len(all_quotes) - 1)
        q = all_quotes[r]
        return q #return this object
