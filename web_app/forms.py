from django import forms
from .models import *


class ContactMessage(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"