from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Entry

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'bg-gray-50 text-gray-600 border border-gray-300 rounded-lg block w-full p-2.5',
            'placeholder': 'name@company.com'
        })
    )
    name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 text-gray-600 border border-gray-300 rounded-lg block w-full p-2.5',
            'placeholder': 'Your Name'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'bg-gray-50 text-gray-600 border border-gray-300 rounded-lg block w-full p-2.5',
            'placeholder': '••••••••••'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'bg-gray-50 text-gray-600 border border-gray-300 rounded-lg block w-full p-2.5',
            'placeholder': '••••••••••'
        })

class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'account', 'username', 'password', 'website', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter title'
            }),
            'account': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter account name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter password'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter website URL'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Enter notes',
                'rows': 4
            }),
        }

