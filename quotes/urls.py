#quotes/urls.py

from django.urls import path 
from .views import HomePageView, QuotePageView , RandomQuotePageView

urlpatterns = [
    path('', RandomQuotePageView.as_view() , name = 'random'), #pick a random quote 
    path('all',HomePageView.as_view(), name='all'), #generic class - home view
    path('quote/<int:pk>' , QuotePageView.as_view(), name = 'quote'),
    path('quote/<int:pk>/update',UpdateQuoteView.as_view(),name = "update_quote"), #update
    path('person/<int:pk>', PersonPageView.as_view(), name = 'person'),
    path('create_quote', CreateQuoteView.as_view(),name = 'create_quote'),
] 