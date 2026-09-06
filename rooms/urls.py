from django.urls import path
from . import views

urlpatterns = [
    path("", views.room_list, name="room_list"),
    path("beds/", views.bed_list, name="bed_list"),
    path("admit/", views.admit_patient, name="admit_patient"),
    path(
        "discharge/<int:bed_id>/",
        views.discharge_patient,
        name="discharge_patient"
    ),
]