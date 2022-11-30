class Hero:
    def __init__(self,name,health,attackPower,armorNumber) -> None:
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name+' menyerang ',lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackLawan):
        print(self.name+' diserang ',lawan.name)
        attackDiterima = attackLawan/self.armorNumber
        print("serangan di terima: ",attackDiterima)
        self.health-=attackDiterima
        print("darah ",self.name," tersisa ",self.health)


hero1 = Hero('sniper',100,10,5)
hero2 = Hero('rikimaru',100,10,10)
hero3 = Hero('ucup',100,10,10)

hero1.serang(hero3)
print("\n")
hero3.serang(hero1)
