# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Documentos(models.Model):
	#edad = models.IntegerField(null = True, blank = True)
	nombre = models.CharField(max_length=100, null = True, blank = True)
	fecha = models.DateTimeField(null = True, blank = True)
	def __unicode__(self):
		return 'Documentos - {0}'.format(self.id)
		