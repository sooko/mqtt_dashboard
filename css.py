from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior

from kivy.uix.label import Label
from kivy.uix.image import Image

Builder.load_string('''
<Btn>:
<BtnHemi>:
    font_name:"fonts/hemi.ttf"
    font_size:self.height/2
    

''')
class Swit(Button):
    pass
class Btn(TouchRippleButtonBehavior,Label):
    pass
class BtnImg(TouchRippleButtonBehavior,Image):
    pass
class LabelHemi(Label):
    font_name="fonts/hemi.ttf"
    halign="left"
    valign="middle"
    # text_size=self.size
class BtnHemi(Btn):
    pass
   

