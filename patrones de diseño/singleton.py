
class Historial:
    __instance1 = None
    def __init__(self):
        if not Historial.__instance1:
            print("__init__method called.")
        else:
            print("Instance already created.", self.getHistorial())
    @classmethod
    def getHistorial(cls):
         if not cls.__instance1:
             cls.__instance1 = Historial()
             return cls.__instance1
s= Historial()
print("Object created:", Historial.getHistorial())


s1 = Historial()

print("Object created:", Historial.getHistorial())
