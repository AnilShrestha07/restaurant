from django import forms
from .models import Order,Booking

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','address','email','paid_amount']
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'date', 'time']
               