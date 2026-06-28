"""Views for the portfolio application."""

from django.views.generic import DetailView, ListView

from .models import Project


class ProjectListView(ListView):
    """Display a list of featured and active projects."""

    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        """Return projects ordered by their configured order."""
        return Project.objects.prefetch_related("tech_stack", "images")


class ProjectDetailView(DetailView):
    """Display the details of a single project."""

    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    