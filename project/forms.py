from django import forms
from .models import Laptop, Profile , Review
class CreateProfileForm(forms.ModelForm):
    '''A form to add new quotes to teh database.'''

    class Meta:
        '''associate this form w Profile model '''
        model = Profile
        fields = ['name','student_id','email', 'phone','laptop'] #which fields from model 

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a profile to the database.'''

    class Meta: 
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['email','phone'] #which fields from model should we use


class CreateReviewForm(forms.ModelForm):
    '''A form to update a status message to the database.'''
    class Meta: 
        '''associate this form with the statusMessage model.'''
        model = Review
        fields = ['person','comment'] #whichfields