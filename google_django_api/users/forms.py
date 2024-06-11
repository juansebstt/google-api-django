from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    """
    Form that uses built-in UserCreationForm to handle user creation
    """
    # First name field
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '*Your first name..', 'id': 'id_first_name'}))

    # Last name field
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Your last name..', 'id': 'id_last_name'}))

    # Email field
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..', 'id': 'id_username'}))

    # Password field
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password', 'id': 'id_password1'}))

    # Confirm password field
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..', 'class': 'password', 'id': 'id_password2'}))

    # reCAPTCHA token
    token = forms.CharField(
        widget=forms.HiddenInput())

    class Meta:
        """
        Meta class for the UserForm.
        """
        # Model that the form is bound to
        model = User

        # Fields that are included in the form
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


# Class that extends AuthenticationForm to handle user authentication
class AuthForm(AuthenticationForm):
    """
    Form that uses built-in AuthenticationForm to handel user auth
    """
    # Email field for user authentication
    username = forms.EmailField(max_length=254, required=True,  # Max length of email
                                widget=forms.TextInput(attrs={'placeholder': '*Email..'}))  # Placeholder text and CSS class for password input

    # Password field for user authentication
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))  # Placeholder text and CSS class for password input

    # Meta class for the AuthForm
    class Meta:
        # Model that the form is bound to
        model = User  # Model that the form is bound to

        # Fields that are included in the form
        fields = ('username', 'password',)  # Fields that are included in the form


class UserProfileForm(forms.ModelForm):
    """
    Basic model-form for our user profile that extends Django user model.
    """
    # Hidden address field
    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    
    # Hidden town field
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    
    # Hidden county field
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    
    # Hidden post code field
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    
    # Hidden country field
    country = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput())
    
    # Hidden longitude field
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    
    # Hidden latitude field
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        # Model that the form is bound to
        model = UserProfile

        # Fields that are included in the form
        fields = ('address', 'town', 'county', 'post_code',
                  'country', 'longitude', 'latitude')
