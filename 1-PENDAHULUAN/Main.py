class Hero:
    pass

hero1 = Hero() # object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 200

print(f"hero1 = {hero1.__dict__}")
print(f"hero2 = {hero2.__dict__}")
print(f"hero3 = {hero3.__dict__}")
print(hero1)