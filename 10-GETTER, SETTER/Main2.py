class Hero:
    def __init__(self,name,health,armor) -> None:
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__inpo = 'name: {}\n\thealth: {}'.format(self.__name,self.__health)

    @property
    def inpo(self):
        return self.__inpo

    @property
    def health(self):
        pass
    @health.getter
    def health(self):
        return self.__health
    @health.setter
    def health(self,input):
        self.__health=input
    @health.deleter
    def healteh(self):
        self.__health=None

hero2 = Hero('zilong',100,20)
print(hero2.inpo)
print(hero2.health)
hero2.health=20
print(hero2.health)
del hero2.healteh
print(hero2.health)

