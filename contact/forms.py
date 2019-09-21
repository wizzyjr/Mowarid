from django import forms
from contact.models import contact
# from contact.models import contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'comment']

