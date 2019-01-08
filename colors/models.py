# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Colors(models.Model):
    color_name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.color_name

