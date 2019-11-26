from abc import ABC, abstractclassmethod


class client(Estereo):
    def changeMode(self):
        
    def listenMusic(self):


class Estereo(playMusic):
    @abstractmethod
    def playMusic(self):
        pass

class disc (playMusic):
    def playMusic(self):
        
class RCA(playMusic):
    def playMusic(self):
        
class Aux(RCAadapter):
    def playmusic(self):
        
  
#class Aux(ABC):
    #@abstractmethod
    #def listenMusic(self):
     #   pass

class RCAadapter(playMusic):
    def playMusic(self):

       


        
        
        
        
play = estereo()
