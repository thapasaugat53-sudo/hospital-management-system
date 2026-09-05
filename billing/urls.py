from django.urls import path
from . import views


urlpatterns = [

    path(
        "create/<int:appointment_id>/",
        views.create_bill,
        name="create_bill"
    ),

    path(
        "detail/<int:bill_id>/",
        views.bill_detail,
        name="bill_detail"
    ),

    path(
        "my-bills/",
        views.patient_bills,
        name="patient_bills"
    ),

]