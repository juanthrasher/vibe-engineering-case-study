from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("duration_minutes", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="AvailabilitySlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("starts_at", models.DateTimeField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="slots",
                        to="booking.service",
                    ),
                ),
            ],
            options={"ordering": ["starts_at"]},
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=120)),
                ("customer_contact", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "slot",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="booking",
                        to="booking.availabilityslot",
                    ),
                ),
            ],
            options={"ordering": ["slot__starts_at"]},
        ),
        migrations.AddConstraint(
            model_name="availabilityslot",
            constraint=models.UniqueConstraint(
                fields=("service", "starts_at"),
                name="unique_service_start",
            ),
        ),
    ]
