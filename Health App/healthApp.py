from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Health(BoxLayout):
    pass

class HealthApp(App):
    def build(self):
        return Health()

HealthApp().run()