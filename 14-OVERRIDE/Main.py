class Hero:
    def __init__(self,name,health) -> None:
        self.name=name
        self.health=health
    def info(self):
        print("{} health: {}".format(self.name,self.health))

class HeroIntelegent(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 100)
    def info(self):
        print("{}\n\t tipe = intelegent\n\t health: {}".format(self.name,self.health))

class HeroStrength(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 200)
    def info(self):
        print("{}\n\t tipe = strength\n\t health: {}".format(self.name,self.health))


hero1 = HeroIntelegent('lina')
hero2 = HeroStrength('maya')

hero1.info()
hero2.info()
        