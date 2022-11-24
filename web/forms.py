import re
from logging import PlaceHolder
from secrets import choice

from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput, URLInput, Select, NumberInput, RadioSelect, FileInput, ClearableFileInput, PasswordInput, DateInput

from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('id','client_name','phone1','phone2','email','address','state','district','pincode')
        widgets = {
            'client_name' : TextInput(attrs={'class':'form-control','name':'client_name','placeholder':'Name','required':'required','autocomplete':'off','id':'editname'}),
            'phone1' : TextInput(attrs={'class':'form-control','name':'phone','placeholder':'Phone1','required':'required','autocomplete':'off',}),
            'phone2' : TextInput(attrs={'class':'form-control','name':'phone','placeholder':'Phone2','required':'required','autocomplete':'off',}),
            'email' : EmailInput(attrs={'class':'form-control','name':'email','placeholder':'Email','required':'required','autocomplete':'off',}),
            'address' : TextInput(attrs={'class':'form-control','name':'address','placeholder':'Address','required':'required','autocomplete':'off',}),
            'state' : TextInput(attrs={'class':'form-control','name':'state','placeholder':'State','required':'required','autocomplete':'off',}),
            'district' : TextInput(attrs={'class':'form-control','name':'district','placeholder':'District','required':'required','autocomplete':'off',}),
            'pincode' : TextInput(attrs={'class':'form-control','name':'pincode','placeholder':'Pincode','required':'required','autocomplete':'off',}),            
        }