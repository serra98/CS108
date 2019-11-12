from django.shortcuts import render

# Create your views here.
from .models import mini_fb 
from django.views.generic import ListView , DetailView

class ShowAllProfilesView(ListView):
    '''create a subclass of listview to display all mini_fb'''

    model = mini_fb #retrieve obejcts of type mini_fb from database 
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_mini_fb_list'

class ShowProfilePageView(DetailView):
    '''show the detail for one mini_fb'''
    model = mini_fb
    template_name = 'mini_fb/base.html'
    context_object_name = 'mini_fb'