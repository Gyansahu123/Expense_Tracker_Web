from  django import forms 
from .models  import Expense
from django.contrib.auth.models import User

#registration
class RegisterForm(forms.ModelForm):
  password=forms.CharField(widget=forms.PasswordInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter Password'
  }))

  class Meta:
    model=User
    fields=['username','email','password']
    widgets = {
        'username': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    }

#loginform
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))




#expenseform
class ExpenseForm(forms.ModelForm):
  class Meta:
    model=Expense
    fields=['amount','category','description']
    widgets = {
        'amount': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount'
        }),
        'category': forms.Select(attrs={
            'class': 'form-select'
        }),
        'description': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        }),
    }
