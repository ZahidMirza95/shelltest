import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget

from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasAgg
import matplotlib.pyplot as plt
currency=''

class Crypto(Screen):
    def doSomething(instance,test):
        print(test)
    def update(self,val):
        currency=val
        print(currency)
        test= InfoPage()
        test.ids.infoButton.text

#sm=ScreenManager()

class InfoPage(Screen):
    def __init__(self, **kwargs):
        super(InfoPage, self).__init__(**kwargs)
        #box=self.ids.box
    #def __init__(self, **kwargs):
     #  self.ids.infoButton.text
      #  print(self.ids.infoButton.text)
    
    
        
   # def update(self):
        # self.ids.buttonTwo.text=currency
        #test=self
    pass
x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x,y)
#plt.ylabel("y axis")
#plt.xlabel("x axis")
#plt.show()
   
    



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Crypto.kv")
'''class Crypto(GridLayout):

    def __init__(self, **kwargs):
        super(Crypto, self).__init__(**kwargs)
        
        # populate the RecycleView
        self.ids.coinList.data = [{'value': str(i)} for i in range(20)]'''

class CryptoApp(App):
    value=StringProperty('hello')
    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        
        return kv
        # return Label(text='Hello world')




if __name__ == "__main__":
    cyrptoApp = CryptoApp()
    cyrptoApp.run()
    