from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from accounts.models import Profile
from django.forms import widgets


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'phone_number')
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1':  widgets.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password', 'autocomplete': 'new-password', 'style': 'background-color: #f5f5f5; border: 1px solid #ccc; border-radius: 5px; font-size: 18px; height: 45px;'}),
            'password2': widgets.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'autocomplete': 'new-password'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone_number']
        widgets = {
            'email': widgets.EmailInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Write Your Email Address'
            }),
            'username': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Write new username'
            }),
            'phone_number': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Write new phone number'
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = forms.TypedChoiceField(choices=GENDER_CHOICES, coerce=str)

    class Meta:
        model = Profile
        fields = ('avatar', 'description', 'gender')
        widgets = {
            'avatar': widgets.FileInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Upload avatar'
            }),
            'description': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your description'
            }),
            'gender': widgets.Select(attrs={
                'class': 'form-control mb-3',
            })
        }


class ChangePasswordForm(PasswordChangeForm):
    widgets = {
        'new_password_1': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3'
        }),
        'new_password_2': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3'
        }),
        'old_password': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3'
        }),
    }


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2",
        'name': "search",
        'type': "search",
        'placeholder': "Search",
        'aria-label': "Search"
    }))

