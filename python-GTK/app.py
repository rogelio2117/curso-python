import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, GLib
from ejercicioactpas import MiVentanita

class CursoPythonapp(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super(CursoPythonapp, self).__init__(*args, 
			application_id= 'edu.udem.rogeliocastillo',
			**kwargs
		)
		self.window = None
	def do_activate(self):
		
		if not self.window:
			self.window = MiVentanita(application = self, title = 'ventana principal')
		self.window.show_all()
		self.window.present()

if __name__ == '__main__':
	app = CursoPythonapp()
	app.run()