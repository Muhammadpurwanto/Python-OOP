class Hero:
    # claas variable
    jml = 0
    def __init__(self,inputName,inputHealth,inputPower,inputArmor) -> None:
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.Power = inputPower
        self.armor = inputArmor
        Hero.jml +=1
        print("membuat hero dgn nama:",self.name)
hero1 = Hero("ucup",100,10,4)
print(Hero.jml)
# print(hero1.__dict__)
hero2 = Hero("otong",200,35,2)
print(Hero.jml)
# print(hero2.__dict__)