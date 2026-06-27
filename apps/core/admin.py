"""Admin configuration for the core application."""

from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(TranslatableAdmin):
    """Admin interface for the Profile model."""

    list_display = ("name", "email", "is_active")
    