# Generated by Django 2.2.8 on 2022-01-05 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("smbus", "0010_auto_20210601_1444"),
    ]

    operations = [
        migrations.AlterField(
            model_name="smbusdevice",
            name="instrument_handler",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pyscada.DeviceHandler",
            ),
        ),
    ]
