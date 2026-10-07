from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/<int:appointment_id>/",
        views.create_prescription,
        name="create_prescription"
    ),

    path(
        "history/",
        views.prescription_history,
        name="prescription_history"
    ),

    path(
        "print/<int:prescription_id>/",
        views.print_prescription,
        name="print_prescription"
    ),
]