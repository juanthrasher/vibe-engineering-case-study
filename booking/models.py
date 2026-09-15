from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=120)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class AvailabilitySlot(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="slots",
    )
    starts_at = models.DateTimeField()

    class Meta:
        ordering = ["starts_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["service", "starts_at"],
                name="unique_service_start",
            )
        ]

    def __str__(self):
        return f"{self.service} — {self.starts_at}"


class Booking(models.Model):
    slot = models.OneToOneField(
        AvailabilitySlot,
        on_delete=models.PROTECT,
        related_name="booking",
    )
    customer_name = models.CharField(max_length=120)
    customer_contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["slot__starts_at"]

    @property
    def service(self):
        return self.slot.service

    def __str__(self):
        return f"{self.customer_name} — {self.slot}"
