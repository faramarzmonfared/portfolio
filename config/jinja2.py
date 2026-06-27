"""Jinja2 environment configuration for the portfolio project."""

from typing import Any

from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext
from jinja2 import Environment


def environment(**options: Any) -> Environment:
    """Build and configure the Jinja2 environment.

    Args:
        **options: Keyword arguments passed to the Jinja2 Environment.

    Returns:
        A configured Jinja2 Environment instance.
    """
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "_": gettext,
        }
    )
    return env
