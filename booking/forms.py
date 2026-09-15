from django import forms
from django.utils import timezone

from .models import AvailabilitySlot


class AvailabilitySlotForm(forms.ModelForm):
    starts_at = forms.DateTimeField(
        label="Data e hora",
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={"type": "datetime-local"},
        ),
    )

    class Meta:
        model = AvailabilitySlot
        fields = ["starts_at"]

    def clean_starts_at(self):
        starts_at = self.cleaned_data["starts_at"]
        if starts_at <= timezone.now():
            raise forms.ValidationError("Escolha um horário futuro.")
        return starts_at


class BookingForm(forms.Form):
    customer_name = forms.CharField(label="Nome", max_length=120)
    customer_contact = forms.CharField(label="Contato", max_length=200)
