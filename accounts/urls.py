from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path(
        "dashboard/admin/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "dashboard/doctor/",
        views.doctor_dashboard,
        name="doctor_dashboard"
    ),

    path(
        "dashboard/patient/",
        views.patient_dashboard,
        name="patient_dashboard"
    ),
]