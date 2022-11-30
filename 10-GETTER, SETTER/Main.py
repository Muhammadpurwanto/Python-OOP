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
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor didelet')
        self.__armor = None

hero1 = Hero('miya',100,50)
print(hero1.inpo)

hero1.name='dadang'
print(hero1.inpo)
print('getter dan setter untuk armor')
print(hero1.armor)
hero1.armor=70
print(hero1.armor)
print('delet armor')
del hero1.armor
print(hero1.__dict__)

