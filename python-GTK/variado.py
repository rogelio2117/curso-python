import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MiVentana(Gtk.Window):
    def __init__(self, *args, **kwargs):

        super(MiVentana, self).__init__(*args, **kwargs)
        self.set_default_size(500, 300)
        self.connect('delete-event', Gtk.main_quit)

        self.agregar_contenedor()
        self.agregar_texto()
        self.agregar_boton(
        	)
        self.agregar_label()
        self.contenedor


    def agregar_contenedor(self):
        self.contenedor = Gtk.Grid()
        self.contenedor.set_column_homogeneous(True)
        self.add(self.contenedor)


    def agregar_texto(self):
        self.entrada =  Gtk.Entry()
        self.contenedor.attach(self.entrada, 0, 0, 3, 1)
    

    def agregar_boton(self):
    	self.button = Gtk.Button('Ingresar')
    	self.contenedor.attach(self.button, 1,1,1,1)

    def agregar_label(self):
    	self.label = Gtk.Label('Texto Ingresado')
    	self.contenedor.attach(self.label, 0,0,3,1)


if __name__ == '__main__':



	ventana = MiVentana()
	ventana.show_all()

	Gtk.main()

