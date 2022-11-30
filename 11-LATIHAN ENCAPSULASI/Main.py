class Hero:
    __jumlah = 0
    def __init__(self,name,health,attPower,armor) -> None:
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah+=1

    @property
    def info(self):
        return "{} : \n\tHealth = {}/{} \n\tlevel = {}\n\tattack = {} \n\tarmor  = {}".format(self.__name,self.__health,self.__healthMax,self.__level,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        print(self.__exp)
        if (self.__exp >= 100):
            print(self.__name,'level up')
            self.__level +=1
            self.__exp -=100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self,musuh):
        self.gainExp = 50


hero1 = Hero("slardar",100,5,10)
hero2 = Hero('miya',100,10,5)
print(hero1.info)

hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)

print(hero1.info)