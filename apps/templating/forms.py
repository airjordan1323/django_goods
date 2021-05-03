from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'fio',
            'position',
            'email',
            'phone',
            'message',
        ]

        widgets = {
            "fio": forms.TextInput(attrs={
                'class': 'popup-input'
            }),
            "position": forms.TextInput(attrs={
                'class': 'popup-input'
            }),
            "email": forms.EmailInput(attrs={
                'class': 'popup-input'
            }),
            "phone": forms.TextInput(attrs={
                'class': 'popup-input'
            }),
            "message": forms.Textarea(attrs={
                'class': 'textarea'
            }),
        }
