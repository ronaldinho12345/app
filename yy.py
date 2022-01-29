from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
Window.clearcolor=(0,0,0,1)
Window.size = (400,620)
class Myapp(App):
    def biuld(self):
        self.title="this app has been programmed by taha",
        checkbox=checkBox()
        chekbox.bind(active=click)
        return chekbox
    def click(checkbox,value):
        if value:
            print("male")
        else:
            print("female")
Myapp().run()