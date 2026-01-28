from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import os

class OttoEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # 📂 CONFIGURACIÓN DE LA BASE DE DATOS (NoSQL Local)
        # Buscamos la carpeta interna del celular para que no se borren los datos
        data_dir = App.get_running_app().user_data_dir
        self.store = JsonStore(os.path.join(data_dir, 'otto_vault.json'))

        # 🎨 ESTÉTICA CYBERPUNK
        # Fondo negro profundo
        Window.clearcolor = get_color_from_hex('#0A0A0A')

        # Cabezal con Neón
        self.add_widget(Label(
            text="[b]OTTO-TASK: ONLINE[/b]\n[color=00FFCE]Status: SCANNING...[/color]", 
            markup=True,
            font_size='28sp',
            size_hint_y=0.2,
            halign='center'
        ))

        # Cuerpo central (Aquí irán tus tareas)
        self.display = Label(
            text="Iniciando base de datos...",
            color=get_color_from_hex('#FF00FF') # Rosa Neón
        )
        self.add_widget(self.display)

        # Botón de prueba para el JsonStore
        btn = Button(
            text="SINCRONIZAR TAREA",
            background_color=get_color_from_hex('#00FFCE'),
            size_hint_y=0.2
        )
        btn.bind(on_press=self.guardar_tarea)
        self.add_widget(btn)

        self.cargar_datos()

    def guardar_tarea(self, instance):
        # Guardamos un "documento" en nuestra base local
        self.store.put('tarea_actual', nombre='Finalizar APK', status='En Proceso')
        self.display.text = "¡Tarea guardada en JsonStore! 🦾"

    def cargar_datos(self):
        if self.store.exists('tarea_actual'):
            datos = self.store.get('tarea_actual')
            self.display.text = f"Tarea pendiente: {datos['nombre']}\nEstado: {datos['status']}"
        else:
            self.display.text = "No hay tareas en el sistema local."

class OttoApp(App):
    def build(self):
        self.title = "Otto-task Cyber"
        return OttoEngine()

if __name__ == '__main__':
    OttoApp().run()
        
