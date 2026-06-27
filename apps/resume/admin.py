"""Admin configuration for the resume application."""

from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Education, Experience, Skill


@admin.register(Experience)
class ExperienceAdmin(TranslatableAdmin):
    """Admin interface for the Experience model."""

    list_display = ("role", "company", "start_date", "end_date", "is_current")


@admin.register(Education)
class EducationAdmin(TranslatableAdmin):
    """Admin interface for the Education model."""

    list_display = ("degree", "field_of_study", "start_date", "end_date")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin interface for the Skill model."""

    list_display = ("name", "category", "level", "order")
    list_filter = ("category",)
