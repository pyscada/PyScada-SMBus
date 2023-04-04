from __future__ import unicode_literals

from pyscada.models import Device, DeviceHandler
from pyscada.models import Variable
from . import PROTOCOL_ID

from django.db import models
from django.db.models.signals import post_save
import logging

logger = logging.getLogger(__name__)


class SMBusDevice(models.Model):
    smbus_device = models.OneToOneField(Device, on_delete=models.CASCADE)
    port = models.CharField(default='1', max_length=400, )
    address_choices = [(i, '0x%s/%d' % (hex(i), i)) for i in range(256)]
    address = models.PositiveSmallIntegerField(default=address_choices[0][0], choices=address_choices, null=True)

    protocol_id = PROTOCOL_ID

    def parent_device(self):
        try:
            return self.smbus_device
        except:
            return None

    def __str__(self):
        return self.smbus_device.short_name


class SMBusVariable(models.Model):
    smbus_variable = models.OneToOneField(Variable, on_delete=models.CASCADE)
    information = models.CharField(default='None', max_length=400, )

    protocol_id = PROTOCOL_ID

    def __str__(self):
        return self.smbus_variable.name


class ExtendedSMBusDevice(Device):
    class Meta:
        proxy = True
        verbose_name = 'SMBus Device'
        verbose_name_plural = 'SMBus Devices'


class ExtendedSMBusVariable(Variable):
    class Meta:
        proxy = True
        verbose_name = 'SMBus Variable'
        verbose_name_plural = 'SMBus Variables'
