class Hero:
    def __init__(self,name,health) -> None:
        self.name=name
        self.health=health

class Hero_intelegent(Hero):
    pass

class Hero__agility(Hero):
    pass

hero1 = Hero("miya",100)
hero2 = Hero__agility("samsul",100)
hero3 = Hero_intelegent("nurul",100)

print(hero1.__dict__)
print(hero2.name)
print(help(hero3))