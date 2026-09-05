from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("appointments/", include("appointments.urls")),
    path(
    "medical-records/",
    include("medical_records.urls")
    ),
    path("prescriptions/", include("prescriptions.urls")),
    path(
    "laboratory/",
    include("laboratory.urls")
    ),
    path(
    "pharmacy/",
    include("pharmacy.urls")
    ),
    path("billing/", include("billing.urls")),
]