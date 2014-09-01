from django.contrib.auth.models import User
from django import forms
from quickfeedback.models import Event, Question, Response, UserProfile


	
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
		
	
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
		
class createqform(forms.Form):
	name = forms.CharField(max_length = 20)
	slug = forms.SlugField(max_length = 20)
	q1 = forms.CharField(max_length=100)
	q2 = forms.CharField(max_length=100)
	q3 = forms.CharField(max_length=100)


