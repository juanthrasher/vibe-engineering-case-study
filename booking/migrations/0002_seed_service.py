from django.db import migrations


def seed_service(apps, schema_editor):
    Service = apps.get_model("booking", "Service")
    Service.objects.get_or_create(
        name="Atendimento",
        defaults={"duration_minutes": 60},
    )


def remove_seed_service(apps, schema_editor):
    Service = apps.get_model("booking", "Service")
    Service.objects.filter(
        name="Atendimento",
        duration_minutes=60,
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_service, remove_seed_service),
    ]
