"""Admin configuration for the portfolio application."""

from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Project, ProjectImage, Technology


class ProjectImageInline(admin.TabularInline):
    """Inline editor for ProjectImage within ProjectAdmin."""

    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    """Admin interface for the Project model."""

    list_display = ("slug", "is_featured", "order", "created_at")
    list_filter = ("is_featured",)
    inlines = [ProjectImageInline]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    """Admin interface for the Technology model."""

    list_display = ("name",)
    