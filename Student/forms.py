from django import forms
from Student.models import *
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['username']
        help_texts = {'profile_pic':'Please upload Only a formal Photo',
                      'resume':'Please Keep Updating Your Resume for every Mock'}
        
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        help_texts = {'username':''}
        