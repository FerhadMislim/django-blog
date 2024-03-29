from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
    		    'username', 
    		    'password', 
    		    'email', 
    		    'first_name', 
    		    'last_name'
    	] 

