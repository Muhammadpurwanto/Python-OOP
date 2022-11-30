class Hero():
    def __init__(self,name,health,attPower,armor) -> None:
        self.name=name
        self.health=health
        self.attPower=attPower
        self.armor=armor

    def menyerang(self,lawan):
        print(self.name," menyerang ",lawan.name)
        lawan.diserang(self,self.attPower)
    def diserang(self,lawan,attLawan):
        print(self.name," diserang ",lawan.name)
        attDiterima = attLawan/self.armor
        print("serangan di terima: ",attDiterima)
        self.health -= attDiterima
        print("sisa health: ",self.health)

hero1 = Hero("maya",100,10,5)
hero2 = Hero("luna",100,5,10)

hero1.menyerang(hero2)
print("\n\n")
hero2.menyerang(hero1)