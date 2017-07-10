import gi 

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(btn):
	print btn
	print 'HOLA MUNDO'


if __name__ == '__main__':

	ventana = Gtk.Window(title='Ejemplo1')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Botn 1')
	boton.connect('clicked', imprimir_algo)
	boton2 =Gtk.Button('Boton 2')
	boton3 =Gtk.Button('Boton 3')
	boton4 =Gtk.Button('Boton 4')

	
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
		boton, #elemento
		0, #columna
		0, #fila
		3, #nro columnas a usar
		1, #nro de filas a usar

	)
	contenedor.attach(boton2,1,1,1,1)
	contenedor.attach(boton3,2,1,1,1)
	contenedor.attach(boton4,0,3,1,1)
	ventana.add(contenedor)


	ventana.show_all()

	Gtk.main()

