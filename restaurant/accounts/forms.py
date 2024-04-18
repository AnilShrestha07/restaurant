from django import forms
from .models import Order
from django.contrib.auth.models import User

class UserCreationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'useranme', 'email', 'password1','password2'] 
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'description',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'label': 'kl'}),
            'description': forms.Textarea(attrs={'class': 'form-control fixed-width ', 'rows': 4, 'placeholder': 'Enter description'}),
        }
        labels = {
            'title': '',  # Set label to an empty string
            'description': '',  # Set label to an empty string
        }
        