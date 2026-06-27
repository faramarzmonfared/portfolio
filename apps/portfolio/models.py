"""Models for the portfolio application."""

from django.db import models
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from parler.models import TranslatableModel, TranslatedFields
from cloudinary.models import CloudinaryField


class Technology(models.Model):
    """Represents a technology used in a project."""

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        """Return the technology name."""
        return self.name


class Project(TranslatableModel):
    """Represents a portfolio project."""

    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        overview=models.TextField(),
        detail_content=MarkdownxField(),
        challenges=MarkdownxField(blank=True),
        result=MarkdownxField(blank=True),
    )

    slug = models.SlugField(unique=True)
    tech_stack = models.ManyToManyField(Technology, related_name="projects")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    cover_image = CloudinaryField("cover image", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateField()

    class Meta(TranslatableModel.Meta):
        """Meta options for Project."""

        ordering = ["order"]

    def __str__(self) -> str:
        """Return the project's display title."""
        return str(self.safe_translation_getter("title", default=self.slug))


class ProjectImage(models.Model):
    """Represents a gallery image for a project."""

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = CloudinaryField("project image")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta options for ProjectImage."""

        ordering = ["order"]

    def __str__(self) -> str:
        """Return a readable representation of the project image."""
        return f"{self.project} - image {self.order}"
    