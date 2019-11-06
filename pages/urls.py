# pages/urls.py

from django.urls import path 
from .views import homePageView # our response function 

urlpatterns = [
    #map the URL to the function homePageView
    path('', homePageView, name = 'home')
]