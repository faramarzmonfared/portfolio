"""Views for the contact application."""

import logging

from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactMessageForm
from .models import ContactMessage

logger = logging.getLogger(__name__)


class ContactCreateView(CreateView):
    """Handle display and submission of the contact form."""

    model = ContactMessage
    form_class = ContactMessageForm
    template_name = "contact/contact.html"
    success_url = reverse_lazy("contact:contact")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Save the message and notify the user of success.

        Args:
            form: The validated contact form.

        Returns:
            The HTTP response redirecting to the success URL.
        """
        response = super().form_valid(form)
        logger.info("New contact message received from %s", form.instance.email)
        messages.success(self.request, "Your message has been sent.")
        return response
    