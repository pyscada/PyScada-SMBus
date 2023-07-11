# Generated by Django 2.2.8 on 2021-06-01 09:38

from django.db import migrations, models
import logging

logger = logging.getLogger(__name__)


def move_device_handlers(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Device = apps.get_model("smbus", "SMBusDevice")
    count = 0
    for item in Device.objects.using(schema_editor.connection.alias).all():
        item.smbus_device.instrument_handler = item.instrument_handler
        item.smbus_device.save()
        count += 1

    logger.info("moved %d SMbus Handler\n" % count)


class Migration(migrations.Migration):
    dependencies = [
        ("smbus", "0011_auto_20220105_1013"),
        ("pyscada", "0100_device_instrument_handler"),
    ]

    operations = [
        migrations.RunPython(
            move_device_handlers, reverse_code=migrations.RunPython.noop
        ),
    ]
