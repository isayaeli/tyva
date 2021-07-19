from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Profile


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'Enter username'}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Enter password'}), label='Password')



class registerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='email')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Last Name')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password2')


    class Meta:
    	model = User
    	fields = ('username','email','first_name','last_name','password1','password2')

    	def save(self, commit=True):
    		user = super(registerForm, self).save(commit=False)
    		user = self.cleaned_data['email']
    		if commit:
    			user.save()
    		return user


class userForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round','placeholder':'username'}), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-round','placeholder':'email'}), label='email')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round','placeholder':'First Name'}), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round',
    'placeholder':'Last Name'}), label='Last Name')
    password = None

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')



USER_STATUS = (
    ('Manager','Manager'),
    ('Not a Manager','Not a Manager')
)
class profileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-round'}),label='Profile Photo')
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-round'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-round'}))
    # user_status = forms.ChoiceField( choices = USER_STATUS, widget=forms.Select(attrs={'class':'form-control form-control-round'}))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude =('user','created','user_status', 'slug')