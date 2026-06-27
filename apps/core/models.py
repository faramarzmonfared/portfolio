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


class SocialLink(models.Model):
    """Represents a social media link attached to a profile."""

    class Platform(models.TextChoices):
        """Supported social media platforms."""

        GITHUB = "GITHUB", "GitHub"
        LINKEDIN = "LINKEDIN", "LinkedIn"
        TELEGRAM = "TELEGRAM", "Telegram"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        FACEBOOK = "FACEBOOK", "Facebook"

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="social_links"
    )
    platform = models.CharField(max_length=20, choices=Platform.choices)
    url = models.URLField()
    label = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta options for SocialLink."""

        ordering = ["order"]

    def __str__(self) -> str:
        """Return a readable representation of the social link."""
        return f"{self.profile.name} - {self.platform}"
    