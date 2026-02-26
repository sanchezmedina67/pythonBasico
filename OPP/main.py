from Enemigo import *
from Zoombie import *
from Ogro import * 

Zoombie = Zoombie(10,1)
ogro = ogro (20,3)

print(f"{Zoombie.get_tipo_enemigo()} tiene {Zoombie.puntos_energia} de energia y ataca con {Zoombie.ataque}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}") 