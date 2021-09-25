import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Crypto(Screen):
        pass
class InfoPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class Crypto(GridLayout):

    def __init__(self, **kwargs):
        super(Crypto, self).__init__(**kwargs)
        
        # populate the RecycleView
        self.ids.coinList.data = [{'value': str(i)} for i in range(20)]

kv = Builder.load_file("Crypto.kv")
class CryptoApp(App):

    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        return kv
        # return Label(text='Hello world')




if __name__ == "__main__":
    cyrptoApp = CryptoApp()
    cyrptoApp.run()
    