# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class remotedevice(models.Model):
    deviceid = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    ipeth0 = models.CharField(max_length=16)
    ipeth1 = models.CharField(max_length=16)
    internet_ip = models.CharField(max_length=16)



        