from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self,set_link) -> None:
        self.link = set_link
    @abstractmethod
    def click(self):
        pass
    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    def click(self):
        print("Go to: {}".format(self.link))

    @Button.link.setter
    def link(self,input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link


tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()
# tombol1.link("www.google.com")
# print(tombol1.link())