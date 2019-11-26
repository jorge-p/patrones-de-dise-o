
from abc import ABC, abstractclassmethod



class client(OriginatorD, CaretakerD):
    pass
        
class OriginatorD(mementoD):
    def stateDoc(self):
        print("call method") 
    def createMemento(self):
        print("call method")
    def saveDoc(self):
        print("call method")  


class mementoD:
    def stateDoc(self):
        print("call method")
    def getState(self):
        print("call method")
    def memento(self):
        print("call method")


class CaretakerD(mementoD):
    def __init__(self):
        self._memento = mementoD()
    def addMementoDoc(self):
        print("call memento method")
    def getMementoDocA(self):
        print("call memento method")


client1 = client()
