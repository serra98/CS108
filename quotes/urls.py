#quotes/urls.py

from django.urls import path 
from .views import HomePageView, QuotePageView , RandomQuotePageView

urlpatterns = [
    path('', RandomQuotePageView.as_view() , name = 'random'), #pick a random quote 
    path('all',HomePageView.as_view(), name='home'), #generic class - home view
    path('quote/<int:pk>' , QuotePageView.as_view(), name = 'quote'),
] 