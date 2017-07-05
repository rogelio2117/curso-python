# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
#importar clase base para vistas
#las vistas manejan la logica del sitio web
from django.views.generic import View
#metoso render retorna una respuesta
#combina una plantilla con un diccionario de contexto
#y retorna un objeto HttpResponse
from django.shortcuts import render
from documentos.models import Documento
#crear vistas de documentos
#definir metodo get



class Documentos(View):
	def get(self, request, *args, **kwargs):
		docs = Documento.objects.all()

		context = {
		'docs':docs,
		'encabezado': 'Mis Documentos'

		}

		return render (request, 'documento.html', context)
		