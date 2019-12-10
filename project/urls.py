
# project/urls.py

from django.urls import path 
from .views import ShowAllLaptopsView , ShowLaptopPageView , create_review , ShowProfilePageView, UpdateProfileView, HomePageView,  CreateProfileView , ShowAllRentalPageView #our view class definition

urlpatterns = [
    path('laptop',ShowAllLaptopsView.as_view(), name='show_all_laptops'), #generic class - base view 
    path('laptop/<int:pk>',ShowLaptopPageView.as_view(), name='show_laptop_page' ),#show one quote
    path('profile/<int:pk>',ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('rental',ShowAllRentalPageView.as_view(), name = 'rental_page'),
    path('',HomePageView.as_view(), name = 'home'),
    path('profile/<int:pk>/update',UpdateProfileView.as_view(), name = 'update_profile'),
    path('create_profile',CreateProfileView.as_view(),name='create_profile'),
    path('laptop/<int:pk>/post_review',create_review,name = 'post_review'),
] 