from Enemigo import *

class ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataques=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataques=ataques)

    def habla(self):
        print("Ogro aplastar todo!!!")
