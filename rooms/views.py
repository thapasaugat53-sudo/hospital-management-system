from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.decorators import receptionist_required
from .models import Room, Bed
from django.shortcuts import get_object_or_404
from .forms import AdmissionForm


@receptionist_required
def room_list(request):
    rooms = Room.objects.all().prefetch_related("beds")

    for room in rooms:
        room.total_beds = room.beds.count()
        room.occupied_beds = room.beds.filter(
            is_occupied=True
        ).count()
        room.available_beds = (
            room.total_beds - room.occupied_beds
        )

        if room.available_beds > 0:
            room.current_availability = "Available"
        else:
            room.current_availability = "Full"

    return render(
        request,
        "rooms/room_list.html",
        {"rooms": rooms}
    )


@receptionist_required
def bed_list(request):
    beds = Bed.objects.all().select_related(
        "room",
        "patient__user"
    )

    return render(
        request,
        "rooms/bed_list.html",
        {"beds": beds}
    )

@receptionist_required
def admit_patient(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)

        if form.is_valid():
            patient = form.cleaned_data["patient"]
            bed = form.cleaned_data["bed"]

            if bed.is_occupied:
                return redirect("admit_patient")

            bed.patient = patient
            bed.is_occupied = True
            bed.save()

            return redirect("bed_list")

    else:
        form = AdmissionForm()

    return render(
        request,
        "rooms/admit_patient.html",
        {"form": form}
    )

@receptionist_required
def discharge_patient(request, bed_id):
    bed = get_object_or_404(Bed, id=bed_id)

    bed.patient = None
    bed.is_occupied = False
    bed.save()

    return redirect("bed_list")