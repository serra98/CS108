#quotes/urls.py 

from django.urls import path 
from .views import HomePageView, QuotePageView , RandomQuotePageView  ,PersonPageView #our class definition

urlpatterns = [
    # map the URL (empty string) to the view 
    path('',RandomQuotePageView.as_view(),name = 'random'),
    path('all', HomePageView.as_view(), name = 'home'),
    path('quote/<int:pk>',QuotePageView.as_view(), name = 'quote'),
    path('person/<int:pk>',PersonPageView.as_view(), name = 'person'),
]