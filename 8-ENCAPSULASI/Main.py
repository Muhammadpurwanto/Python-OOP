class Hero:
    def __init__(self,name,health,attackPower) -> None:
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self,attackMusuh):
        print(self.__name," diserang ",attackMusuh.__name)
        self.__health -= attackMusuh.__attPower

    def setAttackPower(self,nilaiBaru):
        self.__attPower = nilaiBaru

# awal dari game
hero1 = Hero('lusi',100,5)
hero2 = Hero('maya',100,5)

# game berjalan
print(hero1.__dict__)
print(hero1.getName())
print(hero1.getHealth())
hero1.diserang(hero2)
print(hero1.getHealth())


