"""Models for the resume application."""

from django.db import models
from markdownx.models import MarkdownxField
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import MaxValueValidator, MinValueValidator


class Experience(TranslatableModel):
    """Represents a work experience entry."""

    translations = TranslatedFields(
        company=models.CharField(max_length=200),
        role=models.CharField(max_length=200),
        description=MarkdownxField(),
        location=models.CharField(max_length=100, blank=True),
    )

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    class Meta(TranslatableModel.Meta):
        """Meta options for Experience."""

        ordering = ["-start_date"]

    def __str__(self) -> str:
        """Return a readable representation of the experience."""
        return str(self.safe_translation_getter("company", default="Experience"))


class Education(TranslatableModel):
    """Represents an educational background entry."""

    translations = TranslatedFields(
        institution=models.CharField(max_length=200),
        degree=models.CharField(max_length=200),
        field_of_study=models.CharField(max_length=200),
        location=models.CharField(max_length=100, blank=True),
    )

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta(TranslatableModel.Meta):
        """Meta options for Education."""

        ordering = ["-start_date"]

    def __str__(self) -> str:
        """Return a readable representation of the education entry."""
        return str(self.safe_translation_getter("institution", default="Education"))


class Skill(models.Model):
    """Represents a single skill with a proficiency level."""

    class Category(models.TextChoices):
        BACKEND = "BACKEND", "Backend"
        FRONTEND = "FRONTEND", "Frontend"
        DESKTOP = "DESKTOP", "Desktop"
        DATA = "DATA", "Data Analysis"       
        AI_ML = "AI_ML", "AI & Automation"   
        DEVOPS = "DEVOPS", "DevOps"
        TOOLS = "TOOLS", "Tools"             
        OTHER = "OTHER", "Other"

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta options for Skill."""

        ordering = ["category", "order"]

    def __str__(self) -> str:
        """Return the skill name."""
        return self.name
    