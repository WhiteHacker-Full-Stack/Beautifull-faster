from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('ism', 'familiya', 'foto', 'tug_sana', 'bio', 'nomer')

class PasswordForm(forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def validate(self,form):
        password1 = form['password1']
        password2 = form['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwordlar bir xil bolishi kerak ukam")
        return form
