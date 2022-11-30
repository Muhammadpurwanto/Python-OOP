class Hero:
    # private class Variable
    __jumlah = 0
    def __init__(self,name) -> None:
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objec
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objec
    # tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # static mthod
    # bisa class dan objec
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # class method
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

hero1 = Hero('maya')
print(Hero.getJumlah2())
print(hero1.getJumlah3())
hero2 = Hero('salma')
