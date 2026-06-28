"""Jinja2 environment configuration for the portfolio project."""

from typing import Any

import markdown as markdown_lib
from django.forms.boundfield import BoundField
from django.middleware.csrf import get_token
from django.templatetags.static import static
from django.urls import reverse, translate_url
from django.utils.safestring import mark_safe
from django.utils.translation import gettext
from jinja2 import Environment

import jdatetime


def translated_path(path: str, language_code: str) -> str:
    """Translate a URL path into the given language.

    Args:
        path: The current request path.
        language_code: The target language code.

    Returns:
        The equivalent path translated to the target language.
    """
    return translate_url(path, language_code)


def add_class(field: BoundField, css_class: str) -> str:
    """Render a form field with an additional CSS class.

    Args:
        field: The bound form field to render.
        css_class: The CSS class string to apply.

    Returns:
        The rendered HTML for the field with the class applied.
    """
    return field.as_widget(attrs={"class": css_class})


def csrf_input(request) -> str:
    """Generate a hidden CSRF input field for forms.

    Args:
        request: The current HTTP request.

    Returns:
        An HTML-safe hidden input string containing the CSRF token.
    """
    token = get_token(request)
    return mark_safe(f'<input type="hidden" name="csrfmiddlewaretoken" value="{token}">')


def format_date(date: Any, language_code: str = "en") -> str:
    """Format a date according to the active language.

    Args:
        date: The date object to format.
        language_code: The current language code.

    Returns:
        A formatted date string, in Jalali for Persian, Gregorian otherwise.
    """
    if not date:
        return ""
    if language_code == "fa":
        jalali_date = jdatetime.date.fromgregorian(date=date)
        return jalali_date.strftime("%Y/%m/%d")
    return date.strftime("%Y-%m-%d")


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
            "csrf_input": csrf_input,
            "translated_path": translated_path
        }
    )
    env.filters["markdown"] = render_markdown
    env.filters["jalali_date"] = format_date
    env.filters["add_class"] = add_class
    return env
