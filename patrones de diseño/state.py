

from abc import ABC, abstractclassmethod

class TCPstate (ABC):
    @abstractmethod
    def open(self):
        pass
    def Close(self):
        pass
    def recognizing(self):
        pass

class TCPestablished(TCPstate):
    def open(self):
        print("open TCPestablished")
    def close(self):
        print("close TCPestablished")
    def recognizing(self):
        print("recognizing TCPestablished")
    
class TCPListen(TCPstate):
    def open(self):
        print("open TCPListen")
    def close(self):
        print("close TCPListen")
    def recognizing(self):
        print("recognizing TCPListen")

class TCPclosed(TCPstate):
    def open(self):
        print("open TCPclosed")
    def close(self):
        print("close TCPclosed")
    def recognizing(self):
        print("recognizing TCPclosed")

class TCPconnection:
    def __init__(self):
        self._TCPstate = TCPstate()
