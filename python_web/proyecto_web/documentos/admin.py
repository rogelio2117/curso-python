# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#importar modelo 
from documentos.models import Documentos

#crear subclase de admin 
class DocumentoAdmin(admin.ModelAdmin):
	model = Documentos

#registrar model admin
admin.site.register(Documentos, DocumentoAdmin)
