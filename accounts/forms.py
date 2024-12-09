from typing import Any, Mapping
from django import forms
from django.core import validators
from .models import Address, Profile, User
from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({"class":"form-control", "name":"next"}))
    password = forms.CharField(max_length=80,widget=forms.PasswordInput({"class":"form-control"}))


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control"}),validators=[validators.MinLengthValidator(5)])
    password2 = forms.CharField(widget=forms.PasswordInput({"class":"form-control"}),validators=[validators.MinLengthValidator(5)])
    
    def clean(self):
        cleaned = super().clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise ValidationError("پسورد ها مشابه نیست",code="passwords_same")
        return cleaned
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("این کاربر قبلا ثبت نام کرده است",code="user_exist")
        return email


def start_with_0(value):
    if value[0] != '0':
        raise ValidationError("شماره باید با صفر شروع شود",code="value_0")
    return value


class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)    
    
    class Meta:
       model = Address
       fields = "__all__"
       
       widgets = {
            "city":forms.TextInput({"class":"form-control"}),
            "province":forms.TextInput({"class":"form-control"}),
            "email":forms.TextInput({"class":"form-control"}),
            "phone":forms.TextInput({"class":"form-control","name":"phone","id":"tel"}),
            "address":forms.TextInput({"class":"form-control","name":"address","id":"address"}),
            "receiver":forms.TextInput({"class":"form-control","name":"receiver","id":"receiver"}),
            "zip_code":forms.TextInput({"class":"form-control","name":"zip_code","id":"zip_code"}),
            
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 11:
            raise ValidationError("شماره تماس باید 11 رقم باشد", "len_phone")
        if Address.objects.filter(phone=phone).exists():
            raise ValidationError("این شماره تلفن وجود دارد")
        if not phone.isdigit():
            raise ValidationError("شماره تلفن باید عدد باشد")
        
        if not phone.startswith("09"):
            raise ValidationError("شماره تلفن باید با 09 شروع شود")
        
        return phone
            
            
