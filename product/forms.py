from django import forms

from .models import Contact

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "subject": forms.TextInput({"class":"form-control"}),
            "message": forms.Textarea({"class":"form-control"}),
        }


