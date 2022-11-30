# class abstract
# abc = abstract base class
from abc import ABC,abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass
class PushButton(Button):
    def click(self):
        print("PushButton click")

tombol1 = PushButton()
tombol1.click()

