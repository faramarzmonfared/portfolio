"""Models for the contact application."""

from django.db import models


class ContactMessage(models.Model):
    """Represents a message submitted through the contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        """Meta options for ContactMessage."""

        ordering = ["-created_at"]

    def __str__(self) -> str:
        """Return a readable representation of the contact message."""
        return f"{self.name} - {self.created_at:%Y-%m-%d}"
    