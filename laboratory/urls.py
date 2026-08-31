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

]