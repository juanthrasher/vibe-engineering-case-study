from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import AvailabilitySlotForm, BookingForm
from .models import AvailabilitySlot, Booking, Service


def available_slots(request):
    slots = (
        AvailabilitySlot.objects.filter(
            starts_at__gt=timezone.now(),
            booking__isnull=True,
        )
        .select_related("service")
        .order_by("starts_at")
    )
    return render(request, "booking/available_slots.html", {"slots": slots})


def book_slot(request, slot_id):
    slot = get_object_or_404(
        AvailabilitySlot.objects.select_related("service"),
        pk=slot_id,
    )

    unavailable = slot.starts_at <= timezone.now() or hasattr(slot, "booking")
    if unavailable:
        return render(
            request,
            "booking/book_slot.html",
            {"slot": slot, "form": BookingForm(), "unavailable": True},
            status=409,
        )

    form = BookingForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                Booking.objects.create(
                    slot=slot,
                    customer_name=form.cleaned_data["customer_name"],
                    customer_contact=form.cleaned_data["customer_contact"],
                )
        except IntegrityError:
            form.add_error(None, "Este horário não está mais disponível.")
        else:
            return redirect("booking:available")

    return render(
        request,
        "booking/book_slot.html",
        {"slot": slot, "form": form, "unavailable": False},
    )


def provider_availability(request):
    service = Service.objects.order_by("pk").first()
    form = AvailabilitySlotForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if service is None:
            form.add_error(None, "Nenhum serviço inicial foi configurado.")
        else:
            slot = form.save(commit=False)
            slot.service = service
            try:
                with transaction.atomic():
                    slot.save()
            except IntegrityError:
                form.add_error(
                    "starts_at",
                    "Esse horário já foi disponibilizado para o serviço.",
                )
            else:
                return redirect("booking:provider_availability")

    slots = (
        AvailabilitySlot.objects.select_related("service")
        .order_by("starts_at")
    )
    return render(
        request,
        "booking/provider_availability.html",
        {"form": form, "slots": slots, "service": service},
    )


def provider_bookings(request):
    bookings = Booking.objects.select_related("slot__service").order_by(
        "slot__starts_at"
    )
    return render(
        request,
        "booking/provider_bookings.html",
        {"bookings": bookings},
    )
