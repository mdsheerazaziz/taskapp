# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User)
    task = models.CharField(max_length=127)
    task_description = models.CharField(max_length=511)

    def __str__(self):
        return "{}-{}".format(self.task, self.task_description)

