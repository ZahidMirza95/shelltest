import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Crypto(GridLayout):
    pass


class CryptoApp(App):

    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        return Crypto()
        # return Label(text='Hello world')

if __name__ == "__main__":
    cyrptoApp = CryptoApp()
    cyrptoApp.run()
    