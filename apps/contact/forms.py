"""Forms for the contact application."""

from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """Form for submitting a contact message."""

    class Meta:
        """Meta options for ContactMessageForm."""

        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        