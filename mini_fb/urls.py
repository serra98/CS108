# mini_fb/urls.py

from django.urls import path 
from .views import ShowAllProfilesView , ShowProfilePageView , CreateProfileView , UpdateProfileView  #our view class definition

urlpatterns = [
    path('',ShowAllProfilesView.as_view(), name='show_all_profiles'), #generic class - base view 
    path('profile/<int:pk>',ShowProfilePageView.as_view(), name='show_profile_page' ),#show one profile
    path('profile/<int:pk>/update',UpdateProfileView.as_view(), name = 'update_profile'),
    path('profile/<int:pk>/post_status',ShowProfilePageView.as_view(),name = 'post_status'),
    path('create_profile',CreateProfileView.as_view(),name='create_profile'),
] 