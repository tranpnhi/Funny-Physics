from math import sin, pi, cos, sqrt
from pkgutil import get_data
from pydoc import TextDoc
from kivy.uix.boxlayout import BoxLayout
import csv
from turtle import onclick, onscreenclick, textinput, width
from typing import Text
import kivy 
from kivy.uix.textinput import TextInput
from Projectile_Object import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
import os
  
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
  
# Make an app by deriving from the kivy provided app class
class FunnyPhysics(App):
    hislist=[]
    def build(self):

        self.title = "Funny Physics"
        self.layout = GridLayout(cols = 1, padding = 10, spacing = 5)
        self.layout.add_widget(Image(source="banner.png"))
        self.icon = "logo.png"
    
        self.layout.size_hint = (0.5,0.7)
        self.layout.pos_hint = {"center_x": 0.5, "center_y": 0.5 } 
  
        # Add a button
        self.button = Button(text ="Start", size_hint = (0.15, 0.3), bold = True, background_color = '#21F6F6')
        self.layout.add_widget(self.button)
        self.button2 = Button(text ="Information", size_hint = (0.15, 0.3), bold = True, background_color = '#21F6F6')
        self.layout.add_widget(self.button2)  
        # Attach a callback for the button press event
        self.button.bind(on_press = self.onButtonPress)
        self.button2.bind(on_press = self.onButtonPress2)
        return self.layout
    
    
    def get_data(self):
        if self.a.text == "":
            self.get_a = 0
        else:
            self.get_a = float(self.a.text)
            
        if self.h.text == "":
            self.get_h = 0
        else:
            self.get_h = float(self.h.text)
            
        if self.v.text == "":
            self.get_v = 0
        else:
            self.get_v = float(self.v.text)
            
        if self.c.text == "":
            self.get_c= 0
        else:
            self.get_c = float(self.c.text)

        obj = object(self.get_a, self.get_h, self.get_v, self.get_c)
        return obj


    def btn1_cmd(self, event):
        self.obj = self.get_data()
        return str(self.obj.highestpoint())


    def p_n1(self, event):
        self.n=1
        layout_n1 = GridLayout(cols = 1, padding = 5, spacing = 5)
        layout_n1.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.kq = self.btn1_cmd(None)
        popup_n1_lb = Label(text = self.kq)
    
        layout_n1.add_widget(popup_n1_lb)
        popup_n1 = Popup(title = "Highest point", content = layout_n1, size_hint =(None, None), size = (500,500))
        popup_n1.open()
        
        closeButton1 = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n1.add_widget(closeButton1)
        closeButton1.bind(on_press = popup_n1.dismiss)
        saveButton=Button(text='Save',size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n1.add_widget(saveButton)
        saveButton.bind(on_press=self.save)
                
    def btn2_cmd(self, event):
        obj = self.get_data()
        return str(obj.time_1stper())

    def p_n2(self, event):
        self.n=2
        layout_n2 = GridLayout(cols = 1, padding = 5, spacing = 5)
        layout_n2.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.kq = self.btn2_cmd(None)
        popup_n2_lb = Label(text = self.kq)
    
        layout_n2.add_widget(popup_n2_lb)
        popup_n2 = Popup(title = "Period of time (from the beginning to the highest point)", content = layout_n2, size_hint =(None, None), size = (500,500))
        popup_n2.open()
        
        closeButton2 = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n2.add_widget(closeButton2)
        closeButton2.bind(on_press = popup_n2.dismiss)
        saveButton=Button(text='Save',size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n2.add_widget(saveButton)
        saveButton.bind(on_press=self.save)

    
    def btn3_cmd(self, event):
        obj = self.get_data()
        return str(obj.time_2ndper())

    def p_n3(self, event):
        self.n=3
        layout_n3 = GridLayout(cols = 1, padding = 5, spacing = 5)
        layout_n3.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.kq = self.btn3_cmd(None)
        popup_n3_lb = Label(text = self.kq)
    
        layout_n3.add_widget(popup_n3_lb)
        popup_n3 = Popup(title = "Period of time (from the highest point to the end)", content = layout_n3, size_hint =(None, None), size = (500,500))
        popup_n3.open()
        
        closeButton3 = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n3.add_widget(closeButton3)
        closeButton3.bind(on_press = popup_n3.dismiss)
        saveButton=Button(text='Save',size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n3.add_widget(saveButton)
        saveButton.bind(on_press=self.save)
    
    def btn4_cmd(self, event):
        obj = self.get_data()
        return str(obj.totaltime())

    def p_n4(self, event):
        self.n=4
        layout_n4 = GridLayout(cols = 1, padding = 5, spacing = 5)
        layout_n4.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.kq = self.btn4_cmd(None)
        popup_n4_lb = Label(text = self.kq)
    
        layout_n4.add_widget(popup_n4_lb)
        popup_n4 = Popup(title = "Total time", content = layout_n4, size_hint =(None, None), size = (500,500))
        popup_n4.open()
        
        closeButton4 = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n4.add_widget(closeButton4)
        closeButton4.bind(on_press = popup_n4.dismiss)
        popuplabelhihi = Label(text = "Initial height")
        self.layout.add_widget(popuplabelhihi)
        saveButton=Button(text='Save',size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n4.add_widget(saveButton)
        saveButton.bind(on_press=self.save)

    def btn5_cmd(self, event):
        obj = self.get_data()
        return str(obj.length())

    def p_n5(self, event):
        self.n=5
        layout_n5 = GridLayout(cols = 1, padding = 5, spacing = 5)
        layout_n5.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.kq = self.btn5_cmd(None)
        popup_n5_lb = Label(text = self.kq)
        layout_n5.add_widget(popup_n5_lb)
        popup_n5 = Popup(title = "Distance", content = layout_n5, size_hint =(None, None), size = (500,500))
        popup_n5.open()
        closeButton5 = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n5.add_widget(closeButton5)
        closeButton5.bind(on_press = popup_n5.dismiss)
        saveButton=Button(text='Save',size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout_n5.add_widget(saveButton)
        saveButton.bind(on_press=self.save)

    def save(self,text):
        p='.\Source code\save.csv'
        if os.path.isfile(p):
            with open(p, "a") as f:
                writer = csv.writer(f)
                writer.writerow([self.n,self.a.text,self.h.text,self.v.text,self.c.text,self.kq])
        else:
            with open(p, "a") as f:
                writer = csv.writer(f)
                writer.writerow(['FUNCTION','ANGLE','INITIAL HEIGHT','INITIAL VELOCITY','INITIAL COORDINATE','RESULT'])
                writer.writerow([self.n,self.a.text,self.h.text,self.v.text,self.c.text,self.kq])

    def btn6_cmd(self, event):
        obj = self.get_data()
        obj.simulation()

    def reset_bt(self, event):
        self.a.text = ''
        self.h.text = ''
        self.v.text = ''
        self.c.text = ''
        
    # On button press - Create a popup dialog with a label and a close button
    def onButtonPress(self,button):
        self.superlayout=GridLayout(cols=4)
        layout = GridLayout(cols=1)
        popuplabel = Label(text = "Angle")
        layout.add_widget(popuplabel)  
        popuplabel = Label(text = "Initial height")
        layout.add_widget(popuplabel)
        popuplabel = Label(text = "Initial velocity")
        layout.add_widget(popuplabel)
        popuplabel = Label(text = "Initial coordinate")
        layout.add_widget(popuplabel)

        closeButton = Button(text = "Return", size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout.add_widget(closeButton)

        layout3 = GridLayout(cols=1)
        self.a = TextInput()
        layout3.add_widget(self.a)

        self.h = TextInput()
        layout3.add_widget(self.h)
        
        self.v = TextInput()
        layout3.add_widget(self.v)
        
        self.c = TextInput()
        layout3.add_widget(self.c)

              
        resetButton = Button(text='Reset',size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout3.add_widget(resetButton)
        resetButton.bind(on_press = self.reset_bt)
   

        layout2 = GridLayout(cols = 1,padding = 50, spacing = 5)
        b1 = Button(text = "1",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b1)
        b1.bind(on_press = self.p_n1)
        
        b2 = Button(text = "2",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b2)
        b2.bind(on_press = self.p_n2)
        
        b3 = Button(text = "3",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b3)
        b3.bind(on_press = self.p_n3)
        
        b4 = Button(text = "4",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b4)
        b4.bind(on_press = self.p_n4)
        
        b5 = Button(text = "5",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b5)
        b5.bind(on_press = self.p_n5)
        
        b6 = Button(text = "6",size_hint = (1, 0.5), bold = True, background_color = '#21F6F6')
        layout2.add_widget(b6)
        b6.bind(on_press = self.btn6_cmd)


        self.superlayout.add_widget(layout)
        self.superlayout.add_widget(layout3)
        self.superlayout.add_widget(layout2)

        # Instantiate the modal popup and display
        popup = Popup(title =' ',
                      content = self.superlayout)  
        popup.open()          
        closeButton.bind(on_press = popup.dismiss)


    def onButtonPress2(self, button):
        layout2 = GridLayout(cols = 1, padding = 5, spacing = 20)

        popup2_Label = Label(text = " \nWELCOME TO 'FUNNY PHYSICS' APP "
                 "\nThis is an app which helps raise your interest in learning Physics."
                 "\n"
                 "\nFUNNY PHYSICS has 2 main functions:"
                 "\n"
                 "\n<CALCULATING FUNCTION>"
                 "\n       Button 1: Calculate the highest point"
                 "\n       Button 2: Calculate the period of time from the beginning to when object reaches the highest point."
                 "\n       Button 3: Calculate the period of time from the highest point to the end."
                 "\n       Button 4: Calculate the total time."
                 "\n       Button 5: Calculate how far the object reaches."
                 "\n"
                 "\n<SIMULATING FUNCTION>"
                 "\n       Button 6: Simulate the movement of the projectile object.")
        layout2.add_widget(popup2_Label)
        
        layout2.size_hint = (0.5,0.7)
        close2Button = Button(text = "Return",size_hint =(0.3, 0.2), bold = True, background_color = '#21F6F6')
        layout2.add_widget(close2Button) 
        layout2.pos_hint = {"center_x": 0.5, "center_y": 0.5 } 

        popup2 = Popup(title ='Information',
                      content = layout2)  
        popup2.open() 

        close2Button.bind(on_press = popup2.dismiss)
        
# Run the app
if __name__ == '__main__':
    FunnyPhysics().run()