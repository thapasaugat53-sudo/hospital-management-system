from django.shortcuts import redirect


def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            try:
                role = request.user.profile.role
            except AttributeError:
                return redirect("login")

            if role in allowed_roles:
                return view_func(request, *args, **kwargs)

            # Send user to their own dashboard
            if role == "ADMIN":
                return redirect("admin_dashboard")

            elif role == "DOCTOR":
                return redirect("doctor_dashboard")

            elif role == "PATIENT":
                return redirect("patient_dashboard")

            return redirect("login")

        return wrapper

    return decorator


def admin_required(view_func):
    return role_required(["ADMIN"])(view_func)


def doctor_required(view_func):
    return role_required(["DOCTOR"])(view_func)


def receptionist_required(view_func):
    return role_required(["RECEPTIONIST"])(view_func)


def patient_required(view_func):
    return role_required(["PATIENT"])(view_func)