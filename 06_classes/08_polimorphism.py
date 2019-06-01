from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def dibujar(self):
        pass

class TextBox(UIControl):
    def dibujar(self):
        print("textbox")

class DropDownList(UIControl):
    def dibujar(self):
        print("dropdownlist")

def dibujar(control):
    control.dibujar()

txt = TextBox()
dibujar(txt)

ddl = DropDownList()
dibujar(ddl)