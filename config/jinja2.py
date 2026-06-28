"""Jinja2 environment configuration for the portfolio project."""

from typing import Any

import markdown as markdown_lib
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext
from jinja2 import Environment


def render_markdown(text: str) -> str:
    """Convert markdown text to safe HTML.

    Args:
        text: Raw markdown content.

    Returns:
        Rendered HTML marked as safe for template output.
    """
    html = markdown_lib.markdown(text, extensions=["fenced_code", "tables"])
    return mark_safe(html)


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
    env.filters["markdown"] = render_markdown
    return env
