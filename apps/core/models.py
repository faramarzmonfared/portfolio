"""Models for the core application."""

from cloudinary.models import CloudinaryField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from markdownx.models import MarkdownxField


class Profile(TranslatableModel):
    """Represents the site owner's public profile.

    Only one active instance should exist at a time.
    """

    translations = TranslatedFields(
        tagline=models.CharField(max_length=255),
        bio=MarkdownxField(),
    )

    name = models.CharField(max_length=100)
    avatar = CloudinaryField("avatar", blank=True, null=True)
    resume_file = CloudinaryField("resume", blank=True, null=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Return the profile's display name."""
        return self.name
    