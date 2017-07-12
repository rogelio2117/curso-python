import gi 

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Miventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Miventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.entrada_monto = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,2,1)
		self.contenedor.attach_next_to(
			self.entrada_monto,
			self.entrada,
			Gtk.PositionType.RIGHT,
			1,
			1
		)
	
	def agregar_boton(self):
		self.boton = Gtk.Button('agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			3
		)
		self.boton.connect('clicked', self.agregar_fila)

	def agregar_lista(self):
		
		self.modelo = Gtk.ListStore(str, float)
		#self.modelo.append(['valor1', 1.5])

		self.lista_activos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn(
			'Descripcion',
			descripcion, 
			text=0
		)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			2,
			1
		)

		#self.modelo.append(['valor1', 1.5])

	def agregar_fila(self, btn):
		texto=self.entrada.get_text()
		monto= self.entrada_monto.get_text()
		self.modelo.append([texto, float(monto)])

if __name__ == '__main__':
	ventana = Miventana()
	ventana.show_all()
	Gtk.main()
"""crea un treeView
		1 crear el model de datos Gtk.ListStore(type, type,..., type)
		2crear el widget que contiene o muestra los datos de modelo 
		treeview(<model>)
		3definir las columnas y sus contenidos 
		3.1 crear celda para cada columna de la fila 
		los CellRenderer son widget que sirven para mostrar contenido dentro 
		de otros widgetdependiendo de su tipo.
		3.2 crear columnas (TreeViewColum) del treevie que mostrara los datos 
		usando Cellrenderer widgets como elementos hijos
		args: (titulo, cellrenderer, posiscion en el modelo de la informacion a mostrar)
		3.3 agregar cada TreeViewcolum al treeview widget
		https://github.com/of-curso-python/curso-python
		"""