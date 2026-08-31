from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            role = user.profile.role

            if role == "ADMIN":
                return redirect("admin_dashboard")

            elif role == "DOCTOR":
                return redirect("doctor_dashboard")

            elif role == "PATIENT":
                return redirect("patient_dashboard")

            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def admin_dashboard(request):
    return render(
        request,
        "accounts/admin_dashboard.html"
    )


@login_required
def doctor_dashboard(request):
    return render(
        request,
        "accounts/doctor_dashboard.html"
    )


@login_required
def patient_dashboard(request):
    return render(
        request,
        "accounts/patient_dashboard.html"
    )

