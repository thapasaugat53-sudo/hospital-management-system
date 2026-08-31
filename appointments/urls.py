from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.book_appointment, name="book_appointment"),
    path("my/", views.my_appointments, name="my_appointments"),
    path(
        "doctor/",
        views.doctor_appointments,
        name="doctor_appointments"
    ),
    path(
        "doctor/confirm/<int:appointment_id>/",
        views.confirm_appointment,
        name="confirm_appointment"
    ),
    path(
        "doctor/cancel/<int:appointment_id>/",
        views.cancel_appointment,
        name="cancel_appointment"
    ),
]