from django.urls import path
from . import views


urlpatterns = [

    path(
        "dashboard/",
        views.pharmacy_dashboard,
        name="pharmacy_dashboard"
    ),

    path(
        "medicines/",
        views.medicine_list,
        name="medicine_list"
    ),

    path(
        "medicines/add/",
        views.add_medicine,
        name="add_medicine"
    ),

    path(
        "medicines/<int:medicine_id>/edit/",
        views.edit_medicine,
        name="edit_medicine"
    ),

    path(
        "medicines/<int:medicine_id>/delete/",
        views.delete_medicine,
        name="delete_medicine"
    ),

    path(
        "medicines/<int:medicine_id>/increase-stock/",
        views.increase_stock,
        name="increase_stock"
    ),

    path(
        "medicines/<int:medicine_id>/decrease-stock/",
        views.decrease_stock,
        name="decrease_stock"
    ),

    path(
        "medicines/<int:medicine_id>/dispense/",
        views.dispense_medicine,
        name="dispense_medicine"
    ),

]