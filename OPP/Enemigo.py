class Enemigo:
    tipos_Enemigos: str
    puntos_energia: int = 10
    ataque = 1

    def __init__(self, Tipos_Enemigos, puntos_energia=10, ataque=1):
        self.tipos_Enemigos = Tipos_Enemigos
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.tipos_Enemigos
    
    def habla(self):
        print(f"Yo soy {self.tipos_Enemigos}. preparándome para pelear!!")

    def camina(self):
        print(f"{self.tipos_Enemigos} se mueve cerca de ti!!1")

    def atacar(self):
        print(f"{self.get_tipo_enemigo()} ataca con un {self.ataque} de daño")
    
    def ataque_especial(self):
        print("Enemigo no tiene ataque especial")