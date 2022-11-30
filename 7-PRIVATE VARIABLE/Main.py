class Hero:
    # class variable
    jml = 0
    __privateJml = 0
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health

        # variable private
        self.__private = 'private'

        # variable protected
        self._protected='protected'
    @property
    def priv(self):
        pass
    @priv.setter
    def priv(self,input):
        self.__private=input
    @priv.getter
    def priv(self):
        return self.__private


lina = Hero('lina',100)
print(lina.__dict__)

# print(Hero.privateJml)
lina.priv='public'
print(lina.priv)

