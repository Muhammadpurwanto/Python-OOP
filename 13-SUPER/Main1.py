class Hero:
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
        
    def info(self):
        print("{} dengan health {}".format(self.name,self.health))

class HeroIntelegent(Hero):
    def __init__(self,name) -> None:
        super().__init__(name,100)
        super().info()
class HeroStrength(Hero):
    def __init__(self,name) -> None:
        super().__init__(name,200)
        super().info()

hero1 = HeroIntelegent('santi')
hero2 = HeroStrength('andi')

