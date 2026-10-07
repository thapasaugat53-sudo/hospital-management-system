from django.contrib import admin
from .models import Room, Bed


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "room_number",
        "room_type",
        "floor",
        "is_available",
    )
    list_filter = (
        "room_type",
        "floor",
        "is_available",
    )
    search_fields = ("room_number",)


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = (
        "bed_number",
        "room",
        "patient",
        "is_occupied",
    )
    list_filter = (
        "is_occupied",
        "room",
    )
    search_fields = (
        "bed_number",
        "patient__user__username",
    )