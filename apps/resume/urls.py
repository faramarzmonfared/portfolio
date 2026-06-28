"""URL configuration for the resume application."""

from django.urls import path

from .views import ResumeView

app_name = "resume"

urlpatterns = [
    path("", ResumeView.as_view(), name="resume"),
]
