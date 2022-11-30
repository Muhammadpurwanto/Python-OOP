class Hero:
    __jml = 0
    def __init__(self,name,health,attPower,armor) -> None:
        self.__name = name
        self.__healthStandart = health
        self.__attPowerStandart = attPower
        self.__armorStandart =armor

        self.__level = 1
        self.__exp = 0

        self.__maxHealth = self.__healthStandart * self.__level
        self.__maxAttPower = self.__attPowerStandart * self.__level
        self.__maxArmor = self.__armorStandart * self.__level

        self.__health = self.__maxHealth
        self.__attPower = self.__maxAttPower
        self.__armor = self.__maxArmor

        Hero.__jml +=1

    @property
    def info(self):
        return "{} \n\thealth: {}\n\tattPower: {}\n\tarmor: {}".format(self.__name,self.__health,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp +=addExp
        if self.__exp>=100:
            self.__level +=1
            self.__exp -=100
            print("level up",self.__level)
            print(self.__exp)
    
    def attack(self,lawan):
        self.gainExp=self.__attPower


hero1 = Hero("miya",100,55,5)
hero2 = Hero('leslay',100,5,10)
print(hero1.info)
hero1.attack(hero2)
hero1.attack(hero2)
