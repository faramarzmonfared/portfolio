"""Views for the resume application."""

from typing import Any

from django.views.generic import TemplateView

from .models import Education, Experience, Skill


class ResumeView(TemplateView):
    """Display work experience, education, and skills."""

    template_name = "resume/resume.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Add resume data to the template context.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The context dictionary with experiences, education, and skills.
        """
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all()
        context["educations"] = Education.objects.all()
        context["skills"] = Skill.objects.all()
        return context
    