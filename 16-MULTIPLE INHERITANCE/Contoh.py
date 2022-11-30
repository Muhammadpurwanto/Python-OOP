class Team():
    def setTeam(self,team):
        self.team = team
    def showTeam(self):
        print(self.team)
class Tipe():
    def setTipe(self,tipe):
        self.tipe = tipe
    def showTipe(self):
        print(self.tipe)
    
class Hero(Team,Tipe):
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
    def showName(self):
        print(self.name,self.health)

luna = Hero("luna",100)
luna.setTeam('merah')
luna.setTipe('intelegent')
luna.showName()
luna.showTeam()
luna.showTipe()
