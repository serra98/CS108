# pages/urls.py

from django.urls import path 
from .views import HomePageView # our class definition

urlpatterns = [
    #map the URL to the function homePageView
    #path('', homePageView, name = 'home') #function-based view 
    path('',HomePageView.as_view(), name = 'home') #generic class - base view 
    path('about/',AboutPageView.as_view(), name = 'home') #generic class - base view 
]