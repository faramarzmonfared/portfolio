"""Views for the core application."""

from typing import Any

from django.views.generic import TemplateView

from .models import Profile


class HomeView(TemplateView):
    """Render the portfolio homepage."""

    template_name = "core/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Add the active profile to the template context.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The context dictionary with the active profile.
        """
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(is_active=True).first()
        return context
    