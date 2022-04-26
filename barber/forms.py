from operator import mod
from django import forms
from django.forms import ModelForm
from .models import Resumes, Comments


class BookingForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'booking-form__item', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'booking-form__item', 'placeholder': 'Last Name'}))
    recipient = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'booking-form__item', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'booking-form__item', 'type': 'tel', 'placeholder': 'Phone'}))
    
    
class ResumeForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'join-grid__item'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'join-grid__item'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'join-grid__item'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'join-grid__item'}))
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': 'join-message'}))
    picture = forms.ImageField()
    
    class Meta:
        model = Resumes
        fields = '__all__'
        
class CommentForm(ModelForm):
    client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'client_name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment'}))
    
    class Meta:
        model = Comments
        fields = '__all__'