class Hero:
    def __init__(self,inputName,inputHealth,inputPower,inputArmor) -> None:
        self.name = inputName
        self.health = inputHealth
        self.Power = inputPower
        self.armor = inputArmor
hero1 = Hero("ucup",100,10,4)
hero2 = Hero("otong",200,35,2)
print(hero1.__dict__)
print(hero2.__dict__)