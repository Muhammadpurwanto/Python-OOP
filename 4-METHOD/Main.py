class Hero:
    # class variable
    jml_hero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor) -> None:
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jml_hero += 1

    # void function, method tanpa return
    def siapa(self):
        print(f"namaku adalah {self.name}")

    # method dengan argumen
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("ucup", 100, 200, 300)
hero2 = Hero("otong", 200, 100, 200)
hero3 = Hero("asep", 400, 50, 100)

hero1.siapa()
print(hero2.health)
hero2.healthUp(10)
print(hero2.getHealth())