class Hero:
    def __init__(self,name,health) -> None:
        self.name=name
        self.health=health
    def showInfo(self):
        print("{} dengan health {}".format(self.name,self.health))
class Hero_intelegent(Hero):
    def __init__(self,name) -> None:
        super().__init__(name,100)
        # Hero.__init__(self,name,100)
        super().showInfo()
        
class HeroStrength(Hero):
    def __init__(self, name) -> None:
        super().__init__(name,200)
        super().showInfo()

hero1 = Hero_intelegent('susi')
her2 = HeroStrength('maya')