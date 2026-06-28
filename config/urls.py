"""URL configuration for the portfolio project."""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from apps.core.views import HomeView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("markdownx/", include("markdownx.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("", HomeView.as_view(), name="home"),
    path("projects/", include("apps.portfolio.urls")),
    path("resume/", include("apps.resume.urls")),
    path("contact/", include("apps.contact.urls")),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    