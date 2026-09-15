from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.available_slots, name="available"),
    path("book/<int:slot_id>/", views.book_slot, name="book_slot"),
    path(
        "provider/availability/",
        views.provider_availability,
        name="provider_availability",
    ),
    path(
        "provider/bookings/",
        views.provider_bookings,
        name="provider_bookings",
    ),
]
