
from abc import ABC, abstractmethod

class Gender(ABC):

    @abstractmethod
    def select_gender(self):
        pass

class goodPlayer(ABC):
    def __init__(self, gender):
        self.gender = gender

    @abstractmethod
    def size(self):
        pass

class defense(goodPlayer):
    def __init__(self, gender):
        super(defense, self).__init__(gender)

    def size(self):
        print("choosed to jugador class: the best player. ")
        self.gender.select_gender(self)

class Forward(goodPlayer):
    def __init__(self, gender):
        super(Assasin, self).__init__(gender)

    def size(self):
        print("choosed to jugador class: the best player. ")
        self.gender.select_gender(self)

class Man(Gender):
    def select_gender(self):
        print("Gender choosed: Man")

class Woman(Gender):
    def select_gender(self):
        print("Gender choosed: Woman")

class main():
    jugador = defense(Man)
    jugador.size()
    print(" ")
    jugadora = Forward(Woman)
    jugadora.size()
