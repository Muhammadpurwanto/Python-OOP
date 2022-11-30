class Mangga():
    def __init__(self,name,jumlah) -> None:
        self.name = name
        self.jumlah = jumlah
    def __repr__(self) -> str:
        return "mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)

    def __add__(self,objec):
        return self.jumlah+objec.jumlah

    @property
    def __dict__(self):
        return "__dict__mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)

belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("mana lagi",5)
print(belanja1)
print(belanja2)
print(belanja1+belanja2)
print(belanja1.__dict__)