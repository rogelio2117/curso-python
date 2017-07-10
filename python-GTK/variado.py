 gi importación

gi.require_version ( 'Gtk', '3.0')
Gtk de importación gi.repository

clase MiVentana (gtk.Window):
def __init __ (self, args *, ** kwargs):
super (MiVentana, auto) .__ init __ (* args, ** kwargs)
self.set_default_size (500, 300)
self.connect ( 'delete-evento', Gtk.main_quit)

agregar_contenedor def (self):
self.contenedor = Gtk.Grid ()

Si __name__ == '__main__':

Ventana = MiVentana ()
Ventana = gtk.Window (título = 'Variados')
ventana.connect ( 'delete-evento', Gtk.main_quit)
texto = Gtk.Entry ()
texto.get_text ()
boton = gtk.Button ( 'Boton')
label = gtk.Label ()
label.set_markup ( 'Texto una para contactar')

contenedor = Gtk.Grid ()
contenedor.set_column_homogeneous (True)
contenedor.set_row_homogeneous (Falso)

contenedor.attach (texto, 0, 0, 3, 1)
contenedor.attach (boton, 1, 1, 1, 1)
contenedor.attach (etiqueta, 0, 4, 1, 1)

ventana.add (contenedor)
# Ventana.add (texto)
# Ventana.add (boton)
# Ventana.add (etiqueta)
ventana.show_all ()

Gtk.main () 