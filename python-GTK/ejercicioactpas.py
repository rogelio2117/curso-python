import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentanita(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentanita, self).__init__(*args, **kwargs)
		self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)
		self.add_contenedor()
		self.add_entradaActivo()
		self.add_entradaPasivo()
		self.add_botonActivo()
		self.add_botonPasivo()
		self.add_listaActivo()
		self.add_listaPasivo()
		#self.add_labelA()
		#self.add_labelP()
		#self.add_labelC()

	def add_contenedor(self):	
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def add_entradaActivo(self):	
		self.entradaActivo = Gtk.Entry()
		#self.entrada1.connect('activate', self.add_filaA)
		self.contenedor.attach(self.entradaActivo, 0, 0, 3, 1)
		self.entrada1 = Gtk.Entry()
		self.contenedor.attach(self.entrada1, 3, 0, 1, 1)

	#def add_labelA(self):	
		#self.labelA = 

	def add_entradaPasivo(self):	
		self.entradaPasivo = Gtk.Entry()
		self.contenedor.attach(self.entradaPasivo, 0, 20, 3, 1)
		self.entrada2 = Gtk.Entry()
		self.contenedor.attach(self.entrada2, 3, 20, 1, 1)

	def add_botonActivo(self):	
		self.botonActivo = Gtk.Button('Activos')
		self.contenedor.attach_next_to(self.botonActivo, self.entradaActivo,
			Gtk.PositionType.BOTTOM,
			1,
			1)

		self.botonActivo.connect('clicked', self.add_filaActivo)


	def add_botonPasivo(self):	
		self.botonPasivo = Gtk.Button('Pasivos')
		self.contenedor.attach_next_to(self.botonPasivo, self.entradaPasivo,
			Gtk.PositionType.BOTTOM,
			1,
			2)

		self.botonPasivo.connect('clicked', self.add_filaPasivo)

	def add_listaActivo(self):	
		self.modeloActivo = Gtk.ListStore(str, float)
		self.lista_Activo = Gtk.TreeView(self.modeloActivo)

		descripcionActivo = Gtk.CellRendererText()
		columna_descripcionActivo = Gtk.TreeViewColumn('Descripcion_Activo', descripcionActivo, text=0)
		montoActivo = Gtk.CellRendererText()
		columna_montoActivo = Gtk.TreeViewColumn('Monto_Activo', montoActivo, text=1)

		self.lista_Activo.append_column(columna_descripcionActivo)
		self.lista_Activo.append_column(columna_montoActivo)

		self.contenedor.attach_next_to(self.lista_Activo, self.botonActivo,
			Gtk.PositionType.BOTTOM,
			1,
			1)

	def add_listaPasivo(self):	
		self.modeloPasivo = Gtk.ListStore(str, float)
		self.lista_Pasivo = Gtk.TreeView(self.modeloPasivo)

		descripcionPasivo = Gtk.CellRendererText()
		columna_descripcionPasivo = Gtk.TreeViewColumn('Descripcion_Pasivo', descripcionPasivo, text=0)
		montoPasivo = Gtk.CellRendererText()
		columna_montoPasivo = Gtk.TreeViewColumn('Monto_Pasivo', montoPasivo, text=1)

		self.lista_Pasivo.append_column(columna_descripcionPasivo)
		self.lista_Pasivo.append_column(columna_montoPasivo)

		self.contenedor.attach_next_to(self.lista_Pasivo, self.botonPasivo,
			Gtk.PositionType.BOTTOM,
			1,
			1)

	def add_filaActivo(self, btn):	
		textoActivo = self.entradaActivo.get_text()
		numeroActivo = self.entrada1.get_text()
		self.modeloActivo.append([textoActivo, float(numeroActivo)])

	def add_filaPasivo(self, btn):		
		textoPasivo = self.entradaPasivo.get_text()
		numeroPasivo = self.entrada2.get_text()
		self.modeloPasivo.append([textoPasivo, float(numeroPasivo)])

if __name__ == '__main__':		
	ventana = MiVentanita()
	ventana.show_all()
Gtk.main()