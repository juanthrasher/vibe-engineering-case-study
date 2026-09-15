from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from booking.models import AvailabilitySlot, Booking, Service


class BookingFlowTests(TestCase):
    def setUp(self):
        self.service = Service.objects.get(name="Atendimento")
        self.future = timezone.now() + timedelta(days=1)

    def create_slot(self):
        return AvailabilitySlot.objects.create(
            service=self.service,
            starts_at=self.future,
        )

    def test_provider_can_publish_future_slot(self):
        response = self.client.post(
            reverse("booking:provider_availability"),
            {
                "starts_at": timezone.localtime(self.future).strftime(
                    "%Y-%m-%dT%H:%M"
                )
            },
        )

        self.assertRedirects(
            response,
            reverse("booking:provider_availability"),
        )
        self.assertEqual(AvailabilitySlot.objects.count(), 1)

    def test_published_slot_appears_in_public_availability(self):
        slot = self.create_slot()

        response = self.client.get(reverse("booking:available"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(slot, list(response.context["slots"]))

    def test_customer_can_book_available_slot(self):
        slot = self.create_slot()

        response = self.client.post(
            reverse("booking:book_slot", args=[slot.id]),
            {
                "customer_name": "Ana",
                "customer_contact": "ana@example.test",
            },
        )

        self.assertRedirects(response, reverse("booking:available"))
        booking = Booking.objects.get(slot=slot)
        self.assertEqual(booking.customer_name, "Ana")
        self.assertEqual(booking.customer_contact, "ana@example.test")
        self.assertEqual(booking.service, self.service)

    def test_booked_slot_disappears_from_public_availability(self):
        slot = self.create_slot()
        Booking.objects.create(
            slot=slot,
            customer_name="Ana",
            customer_contact="ana@example.test",
        )

        response = self.client.get(reverse("booking:available"))

        self.assertNotIn(slot, list(response.context["slots"]))

    def test_already_booked_slot_cannot_be_booked_sequentially(self):
        slot = self.create_slot()
        Booking.objects.create(
            slot=slot,
            customer_name="Ana",
            customer_contact="ana@example.test",
        )

        response = self.client.post(
            reverse("booking:book_slot", args=[slot.id]),
            {
                "customer_name": "Bruno",
                "customer_contact": "bruno@example.test",
            },
        )

        self.assertEqual(response.status_code, 409)
        self.assertEqual(Booking.objects.filter(slot=slot).count(), 1)

    def test_nonexistent_slot_returns_404(self):
        response = self.client.post(
            reverse("booking:book_slot", args=[999999]),
            {
                "customer_name": "Ana",
                "customer_contact": "ana@example.test",
            },
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(Booking.objects.count(), 0)

    def test_provider_can_view_booking(self):
        slot = self.create_slot()
        Booking.objects.create(
            slot=slot,
            customer_name="Ana",
            customer_contact="ana@example.test",
        )

        response = self.client.get(reverse("booking:provider_bookings"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana")
        self.assertContains(response, "ana@example.test")
