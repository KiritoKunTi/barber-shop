from django import forms



class BookingForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'booking-form__item', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'booking-form__item', 'placeholder': 'Last Name'}))
    recipient = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'booking-form__item', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'booking-form__item', 'type': 'tel', 'placeholder': 'Phone'}))
    
    