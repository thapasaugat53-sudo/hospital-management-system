from django.urls import path
from . import views


urlpatterns = [
    path(
        "consultation/<int:appointment_id>/",
        views.consultation,
        name="consultation"
    ),
]