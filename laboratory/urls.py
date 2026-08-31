from django.urls import path
from . import views


urlpatterns = [

    path(
        "request/<int:appointment_id>/",
        views.request_lab_test,
        name="request_lab_test"
    ),

    path(
        "tests/",
        views.lab_tests,
        name="lab_tests"
    ),

    path(
        "result/<int:test_id>/",
        views.enter_lab_result,
        name="enter_lab_result"
    ),

    path(
        "my-tests/",
        views.patient_lab_tests,
        name="patient_lab_tests"
    ),

    path(
        "doctor-tests/",
        views.doctor_lab_tests,
        name="doctor_lab_tests"
    ),

]