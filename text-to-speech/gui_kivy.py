#also mobile apps
#pip install kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class achor_layout_demo(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)#all components of anchor
        self.lab = Label(
            text = 'Enter your name'
        )
        self.add_widget(self.lab)

        self.text_ip=TextInput(
            size_hint=(.4,.4)
        )
        self.add_widget(self.text_ip)

class DemoApp(App):
    def build(self):
        return achor_layout_demo()


if __name__ =='__main__':
    app = DemoApp()
    app.run()
