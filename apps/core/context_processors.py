"""Context processors for the core application."""

from datetime import datetime
from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest

from .models import SocialLink


def current_year(request: HttpRequest) -> dict[str, Any]:
    """Provide the current year to all templates.

    Args:
        request: The incoming HTTP request.

    Returns:
        A dictionary containing the current year.
    """
    return {"current_year": datetime.now().year}


def social_links(request: HttpRequest) -> dict[str, QuerySet[SocialLink]]:
    """Provide active social links to all templates.

    Args:
        request: The incoming HTTP request.

    Returns:
        A dictionary containing the queryset of active social links.
    """
    links = SocialLink.objects.filter(is_active=True).select_related("profile")
    return {"social_links": links}
