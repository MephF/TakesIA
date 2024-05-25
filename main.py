from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MainWidget(BoxLayout):
    pass


class InputField(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.temp_text = ''  # Variable para almacenar el texto temporalmente

    # Método para añadir texto al TextInput
    def update_text(self, text):  # Define el método 'update_text' que toma 'text' como parámetro
        self.ids.my_text_input.text += text  # Añade el texto al campo de entrada de texto

    # Método para eliminar el último carácter del TextInput
    def delete_last_char(self):
        current_text = self.ids.my_text_input.text  # Obtiene el texto actual del campo de entrada de texto
        if current_text:  # Si hay texto presente
            self.ids.my_text_input.text = current_text[:-1]  # Elimina el último carácter del texto

    def clear_input_text(self):
        self.temp_text = self.ids.my_text_input.text  # Almacenar el texto en la variable temporal
        print("Texto enviado:", self.temp_text)  # Imprimir el texto en consola para verificación
        self.ids.my_text_input.text = ''  # Limpiar el campo de texto


class CameraField(BoxLayout):
    pass


class PredictedTextField(GridLayout):
    pass


class KeyBoard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        rows = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', '.', ','],
            [' ', 'delete']
        ]

        for row in rows:
            row_layout = BoxLayout()
            for key in row:
                if key == ' ':
                    key_button = Button(text=key, size_hint_x=0.8)
                elif key == 'delete':
                    key_button = Button(text=key, size_hint_x=0.2)
                else:
                    key_button = Button(text=key)
                key_button.bind(
                    on_release=self.key_pressed)  # Vincula la pulsación del botón con el método 'key_pressed'
                row_layout.add_widget(key_button)
            self.add_widget(row_layout)

    # Método para manejar la pulsación de teclas
    def key_pressed(self, instance):  # Define el método 'key_pressed' que toma 'instance' como parámetro
        input_field = App.get_running_app().root.ids.input_field  # Obtiene la instancia del campo de entrada de texto
        if instance.text != 'delete':  # Si el texto del botón no es 'delete'
            input_field.update_text(instance.text)  # Actualiza el texto del campo de entrada de texto
        else:  # Si el texto del botón es 'delete'
            input_field.delete_last_char()  # Elimina el último carácter del texto del campo de entrada de texto


class TalkesIAApp(App):
    pass


TalkesIAApp().run()
