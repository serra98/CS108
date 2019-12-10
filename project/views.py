
from django.shortcuts import render

# Create your views here.
from .models import Laptop , Profile
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView ,UpdateView

from .forms import CreateProfileForm , UpdateProfileForm ,CreateReviewForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllLaptopsView(ListView):
    '''create a subclass of listview to display all laptop'''

    model = Laptop #retrieve obejcts of type laptop from database 
    template_name = 'project/show_all_laptops.html'
    context_object_name = 'all_laptop_list'

class ShowLaptopPageView(DetailView):
    '''show the detail for one laptop'''
    model = Laptop
    template_name = 'project/show_laptop_page.html'
    context_object_name = 'laptop'

class ShowAllRentalPageView(ListView):
    model = Profile 
    template_name = 'project/show_all_rental_page.html'
    context_object_name = 'all_rental_list'

class ShowProfilePageView(DetailView):
    '''show the detail for one profile'''
    model = Profile 
    template_name = 'project/show_profile_page.html'
    context_object_name = 'profile'

class HomePageView(ListView): 
    '''show the homepage'''
    model = Laptop 
    template_name = 'project/home.html'
    context_object_name = 'home_list'
    
class CreateProfileView(CreateView):
    '''A view to create a new quote and save it to tjhe database'''

    form_class = CreateProfileForm
    template_name = 'project/create_profile_form.html'

class UpdateProfileView(UpdateView):
    '''A view to update a new quote and save it to tjhe database'''

    form_class = UpdateProfileForm
    template_name = 'project/update_profile_form.html'
    queryset = Profile.objects.all()

def create_review(request, pk):
    '''
    Process a form submission to post a new review
    '''
    # find the profile that matches the `pk` in the URL
    laptop = Laptop.objects.get(pk=pk)

    form = CreateReviewForm(request.POST or None, request.FILES or None)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        comment = request.POST['comment']
        #image = request.POST['image']

        # save the new status message object to the database
        if form.is_valid():

            cr = form.save(commit = False)
            cr.laptop = laptop
            cr.save()


    # redirect the user to the show_profile_page view
    return redirect(reverse('show_laptop_page', kwargs={'pk': pk}))

