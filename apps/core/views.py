"""Views for the core application."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Render the portfolio homepage."""

    template_name = "core/home.html"
    
